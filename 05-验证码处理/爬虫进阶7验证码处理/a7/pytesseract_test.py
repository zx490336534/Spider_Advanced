#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

from PIL import Image
import pytesseract

# text=pytesseract.image_to_string(Image.open('3.png'), lang='eng')
# print(text)

text=pytesseract.image_to_string(Image.open('6.png'), lang='chi_sim')
print(text)



