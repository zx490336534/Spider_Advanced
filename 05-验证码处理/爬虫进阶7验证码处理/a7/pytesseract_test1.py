#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'
import pytesseract
from PIL import Image

def get_bin_table(threshold=230):
    # 获取灰度转二值的映射table
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table

image = Image.open("6.png")
imgry = image.convert('L')  # 转化为灰度图
table = get_bin_table()
out = imgry.point(table, '1')

text = pytesseract.image_to_string(out, config='digits', lang='chi_sim')
# 去除数字以外的其他字符
fil = filter(str.isdigit, text)
new_text = ''
for i in fil:
    new_text += i
print(new_text)