#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

__author__ = 'Terry'

'''
    this.guideRandom = function () {
        return "xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace
        (/[xy]/g, function (e) {
            var t = 16 * Math.random() | 0,
            n = "x" == e ? t : 3 & t | 8;
            return n.toString(16)
        }).toUpperCase()
    }
    ()

    function (e) {
        # | 0  其实就小数取整 ,   0<=Math.random()<1 ，
        # 最终，这个t 就是一个 :  0<= t < 16
        var t = 16 * Math.random() | 0,
        n = "x" == e ? t : 3 & t | 8;
        return n.toString(16)
    }

    gid的生成
'''

def gid_encrypt():
    s_raw = 'xxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'

    s_ret = ''
    for s in s_raw:
        t = random.randint(0, 16)
        if 'x' == s:
            n = t
            s_ret += hex(n)[-1:]
        elif 'y' == s:
            n =  3 & t | 8
            s_ret += hex(n)[-1:]
        else:
            s_ret += s

    return s_ret.upper()

