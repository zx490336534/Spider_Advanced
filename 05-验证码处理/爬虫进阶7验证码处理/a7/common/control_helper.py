#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import traceback

class RetryException(Exception):
    pass

class RetryOvertimesException(Exception):
    pass

MAX_TRY_NUM = 3

class MyNumberIterator(object):
    def __init__(self, num=MAX_TRY_NUM):
        self.num = num

    def next(self):
        self.num -= 1
        if self.num < 0:
            return False
        else:
            return True

    def __iter__(self):
        return self

class MyTimeIterator(object):
    def __init__(self, t=120):
        self.t = t
        self.start_time = time.time()

    def next(self):
        if time.time() - self.start_time >= self.t:
            return False
        else:
            return True

    def __iter__(self):
        return self

def call_until_success(try_times=10, retry_exceptions=None, sleep_time=.5):
    """

    :param try_times:
    :param sleep_time:
    :param retry_exceptions: 重试的异常列表
    :return:
    """
    all_retry_exceptions = tuple(retry_exceptions + [RetryException])
    def dec(func):
        def __decorator(*args, **kwargs):
            """
            调用fun,直到成功
            """
            times = 0
            while 1:
                try:
                    # do something before call
                    r =  func(*args, **kwargs)
                    # do something after call
                    return r
                except all_retry_exceptions as e:
                    times = times + 1
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    try:
                        print("call_until_success %s:%s" % (e.message, traceback.format_exc()))
                        #print "call_until_success full stack: %s" % format_exception(e)
                        pass
                    except:
                        print("oh my god")

                    if times > try_times:
                        #append_line_to_file(traceback.format_exc(),get_app_path_for_window("error.txt"))
                        raise RetryOvertimesException("[%s]重试次数超过%s,放弃" % (func.__name__, try_times))
                    time.sleep(sleep_time)
                except:
                    print("oh my god 111111")
                    print(traceback.format_exc())
                    raise Exception()

        return __decorator
    return dec