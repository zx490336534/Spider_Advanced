#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import md5
import time

from a7.common.control_helper import call_until_success, RetryException
from a7.common.log_helper import write_log_print

CREATE_URL = 'http://v1-api.ruokuai.com/create.json'
REPORTERROR_URL = 'http://v1-api.ruokuai.com/reporterror.json'

class DaMaException(Exception):
    pass

class Ruokuai:
    def __init__(self, s, user, pwd, soft_id, soft_key, image_type = "3040", write_log=write_log_print, timeout=60):
        """

        :param s:
        :param user:
        :param pwd:
        :param soft_id:
        :param soft_key:
        :param image_type: 打码类型,参考http://ruokuai.com/pricelist.aspx
        :param timeout: 超时时间
        """
        self.write_log = write_log
        self.timeout = timeout
        self.image_type = image_type
        self.s = s
        self.soft_key = soft_key
        self.soft_id = soft_id
        self.pwd = md5(pwd).hexdigest()
        self.user = user

        self.create_data = self._make_data({
            'typeid': image_type,
            'timeout': timeout,
        })

    def _make_data(self, data):
        base_data = {
            'username': self.user,
            'password': self.pwd,
            'softid': self.soft_id,
            'softkey': self.soft_key,
        }
        base_data.update(data)
        return base_data

    @call_until_success()
    def create(self, get_vcode_data_func):
        """提交一个打码任务

        :param get_vcode_data_func: 校验码二进制数据获取函数
        """
        files = {'image': ('a.jpg', get_vcode_data_func())}
        r = ''
        try:
            r = self.s.post(CREATE_URL, data=self.create_data, files=files)
            if not r.text:
                raise RetryException()
            j = r.json()
        except ValueError:
            self.write_log("若快返回异常：[%s]" % r.text)
            time.sleep(1)
            raise RetryException()
        except:
            # traceback.print_exc()
            self.write_log("若快返回异常1：[%s]" % r.text)
            time.sleep(1)
            raise RetryException()
        # try:
        if "Result" in j and "Id" in j:
            self.write_log("若快返回验证码：[%s]" % j["Result"])
            return j["Result"], j["Id"]
        elif "已经损坏或者不是正确的图像格式" in j.get("Error",""):
            time.sleep(1)
            raise RetryException()
        else:
            self.write_log("若快返回异常2：[%s]" % r.text)
            raise DaMaException("若快服务返回异常数据[%s]" % r.text)
        # except:
        #     self.write_log("若快返回异常3：[%s]" % r.text)
        #     raise DaMaException("若快服务返回异常数据1[%s]" % r.text)

    def report_error(self, id):
        """
        im_id:报错题目的ID
        """
        data = self._make_data({
            'id': id,
        })
        r = self.s.post(REPORTERROR_URL, data=data)
        text = r.text
        if "报告成功" in text or "报错成功" in text:
            self.write_log("若快提交验证码错误成功")
            pass
        else:
            self.write_log("若快提交验证码错误失败：" + text)
            raise DaMaException("若快报告错误异常[%s]" % text)

def create_dama(*args, **kwargs):
    return Ruokuai(*args, **kwargs)