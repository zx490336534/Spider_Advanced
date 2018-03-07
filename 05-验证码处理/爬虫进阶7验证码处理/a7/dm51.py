#!/usr/bin/env python
# -*- coding: utf-8 -*-
#by terry

import time
from hashlib import md5

import requests

from a7.common.log_helper import write_log_print


class DM51:
    project_dict = {
        "alipay_reg": "1365",
        "jd_reg": "384"
    }

    url = "http://www.jikesms.com/common/ajax.htm"
    def __init__(self, user, pwd, pid, parent_user="prehisle", delay=60, write_log=write_log_print):
        self.write_log = write_log
        self.parent_user = parent_user
        self.s = requests.session()
        self.pid = DM51.project_dict.get(pid, "ERROR")
        self.pwd = md5(pwd).hexdigest()
        self.user = user
        self.delay = delay

        self.login()

    def set_pid(self, pid):
        if DM51.project_dict.get(pid, ""):
            self.pid = DM51.project_dict.get(pid)
        return DM51.project_dict.get(pid, "")

    def get_pid_by_project(self, pid_key):
        return DM51.project_dict.get(pid_key, "")

    def cancelSMSRecvAll(self):
        data = dict([('action', 'phone:PhoneEventAction'),
                     ('token', self.token),
                     ('event_name_cancelAllRecv', "提交")])
        j = self.post_data(data)
        print("cancelSMSRecvAll:%s" % self.user)

    def post_data(self,data):
        try:
            r = self.s.post(DM51.url, data=data)
            j = r.json()
            return j
        except:
            print("51打码提交数据失败："+r.content)

    def login(self):
        data = dict([('action','user:UserEventAction'),
                     ('event_name_login', '提交'),
                     ('uid', self.user),
                     ('useToken', 'true'),
                     ('password', self.pwd)])
        j = self.post_data(data)
        if j["succeed"]:
            self.token = j["model"]["token"]
            print("[%s]51打码登录成功" % self.user)
        else:
            print("[%s]51打码登录异常:%s" % (self.user,j["model"]["message"]))

    def get_mobile_number(self, pid=""):
        if isinstance([1, 2], list):
            data = dict([('action', "phone:PhoneEventAction"),
                         ('event_name_getPhone', "提交"),
                         ('token', self.token),
                         ('serviceId', pid)])
        else:
            pid = pid or self.pid
            data = dict([('action', "phone:PhoneEventAction"),
                         ('event_name_getPhone', "提交"),
                         ('token', self.token),
                         ('serviceId', pid)])
        j = self.post_data(data)
        if j["succeed"]:
            self.number = j["model"]["phone"]
        else:
            self.write_log("[%s]51打码获取手机异常:%s" % (self.user,j["model"]["message"]))
            self.number = ""
            if "请及时释放没有使用的手机号" in j["model"]["message"]:
                self.cancelSMSRecvAll()
            elif "暂时没有可用的手机号" in j["model"]["message"]:
                time.sleep(10)

        return self.number

    def getVcodeAndHoldMobilenum(self, phone_number="", pid="", next_pid="", delay=30):
        return self.getVcodeAndReleaseMobile(phone_num=phone_number, pid=pid, delay=delay, auto_release=False)

    def getVcodeAndReleaseMobile(self, phone_num="", pid="", delay=None, auto_release=True):
        delay = delay if delay else self.delay
        pid = pid if pid else self.pid
        phone_num = phone_num if phone_num else self.number
        data = dict([('action', 'phone:PhoneEventAction'),
                     ('event_name_getMessage', "提交"),
                     ('partnerId', self.parent_user),
                     ('serviceId', pid),
                     ('token', self.token),
                     ('phone', phone_num)])
        #95188|【支付宝】2014年08月07日，您申请的手机校验码是711942。如非本人操作，请致电95188。
        begin_time = time.time()
        while time.time() - begin_time < delay:
            j = self.post_data(data)
            if j["succeed"]:
                self.write_log("获取到验证码[%s]" % j["model"]["message"])
                if auto_release:
                    self.cancelPhoneNumber(phone_num, pid)
                return j["model"]["message"]
            elif "该手机已释放或已加入黑名单" in j["model"]["message"]:
                return ""
            else:
                self.write_log("[%s]还没收到短信,休息6秒再试" % phone_num)
                time.sleep(6)
        else:
            self.write_log("[%s]超过%d秒还没收到短信" % (phone_num, delay))
            self.cancelSMSRecvAll()
            return ""

    def cancelPhoneNumber(self, phone_num="", pid=""):
        pid = pid if pid else self.pid
        phone_num = phone_num if phone_num else self.number
        data = dict([('phone', phone_num),
                     ('serviceId', pid),
                     ('token', self.token),
                     ('action', "phone:PhoneEventAction"),
                     ('event_name_cancelRecv', "提交")])
        j = self.post_data(data)

        if j["succeed"]:
            self.write_log("addIgnoreList[%s]成功" % phone_num)
        else:
            self.write_log("addIgnoreList[%s]失败:%s" % (phone_num,j["model"]["message"]))

        self.number = "" if phone_num == self.number else self.number
        return "1"

    def addIgnoreList(self, phone_num="", pid=""):
        pid = pid if pid else self.pid
        phone_num = phone_num if phone_num else self.number
        data = dict([('phone', phone_num),
                     ('serviceId', pid),
                     ('token', self.token),
                     ('action', "phone:PhoneEventAction"),
                     ('event_name_addBlacklist', "提交")])
        j = self.post_data(data)

        if j["succeed"]:
            self.write_log("addIgnoreList[%s]成功" % phone_num)
        else:
            self.write_log("addIgnoreList[%s]失败:%s" % (phone_num,j["model"]["message"]))

        self.number = "" if phone_num == self.number else self.number
        return "1"

def create_mobile_dama(**kwargs):
    return DM51(**kwargs)

def main():
    d = {
        "a": 1,
        "b": 2,
        "c": 3
    }

    d.update({"d":4, "d1":4})

    # account_info ={ "user": "prehisle",
    #                 "pwd": "D61505",
    #                 "pid": "2118"}
    #
    # m = DM51(**account_info)
    # print m.get_mobile_number()
    # print m.getVcodeAndReleaseMobile()
    # m.addIgnoreList()
    # m.cancelSMSRecvAll()
    pass

if __name__ == '__main__': main()


