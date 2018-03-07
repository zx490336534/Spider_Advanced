#!/usr/bin/env python
# -*- coding: utf-8 -*-
import execjs

__author__ = 'Terry'

# 这里只是示例，告诉大家，纯js加密的函数，
# 通过execjs调用，可以节约时间和精力，不需要进行分析了
# 这下面的代码，不能执行，只是一个示例！！！

js = '''
function s(e, t, n, i, s, o) {
    for (var r = 32767 & t, a = t >> 15; --o >= 0; ) {
        var c = 32767 & this[e]
          , l = this[e++] >> 15
          , d = a * c + l * r;
        c = r * c + ((32767 & d) << 15) + n[i] + (1073741823 & s),
        s = (c >>> 30) + (d >>> 15) + a * l + (s >>> 30),
        n[i++] = 1073741823 & c
    }
    return s
}
'''
pwd = '123456'
ctx = execjs.compile(js)
b = ctx.call('s', pwd)
print(b)