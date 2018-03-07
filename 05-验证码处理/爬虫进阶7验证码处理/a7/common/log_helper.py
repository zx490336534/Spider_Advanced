#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

def write_log_print(str):
    print(str)

def write_log_print_add_time(str):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+":"+str)

def write_log_nothing(str):
    pass
