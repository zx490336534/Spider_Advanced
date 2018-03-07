#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import execjs

# 最基本的使用，执行js代码
# print(execjs.eval("'red yellow blue'.split(' ')"))


# 获取默认的execjs对象，然后通过eval执行js代码
# ctx = execjs.get()
# a = ctx.eval("1 + 2")
# print(a)

# 执行js代码中指定的函数
# ctx = execjs.compile("""
# function add(x, y) {
#     return x + y;
# }
# """)
# b = ctx.call('add', 1, 2)
# print(b)


# 执行js代码中指定的函数，js中函数可以相互调用，可以包含复杂的js块
ctx = execjs.compile("""
function add(x, y) {
    return x + test(y);
}

function test(x){
    return 2*10;
}
""")
b = ctx.call('add', 1, 2)
print(b)