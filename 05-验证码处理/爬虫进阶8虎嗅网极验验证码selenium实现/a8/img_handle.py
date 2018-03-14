#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

import time

__author__ = 'Terry'

import PIL.Image as image
import re
import io
from urllib.request import urlopen

def get_merge_image(file, location_list):
    '''
    根据位置对图片进行合并还原
    :file:图片
    :location_list:图片位置
    '''
    # 用image加载图片
    im = image.open(file)

    im_list_upper=[]
    im_list_down=[]

    # 根据52个div的x和y坐标，进行循环，把打乱了的图切割成52个小图片
    for location in location_list:
        if location['y'] == -58:
            # 宽度必须为10，  修改为12的话，会有干扰空隙，可以保存图片查看区别
            im_list_upper.append(im.crop((abs(location['x']), 58, abs(location['x']) + 10, 116)))
        elif location['y'] == 0:
            im_list_down.append(im.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

    # 建立一个新的图片
    new_im = image.new('RGB', (260, 116))

    x_offset = 0
    # 根据下图片列表，把小图片按照 x和y坐标，粘贴到 new_im
    for im in im_list_upper:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    x_offset = 0
    # 根据下图片列表，把小图片按照 x和y坐标，粘贴到 new_im
    for im in im_list_down:
        new_im.paste(im, (x_offset,58))
        x_offset += im.size[0]

    # new_im.save(str(time.time())+".jpg")
    return new_im


def get_image(driver, div_xpath):
    '''
    下载并还原图片
    :driver:webdriver
    :div:图片的div
    '''

    #找到图片所在的div
    for _ in range(5):
        # 使用的 find_elements_by_xpath , elements是有 s的，复数的div
        background_image_divs=driver.find_elements_by_xpath(div_xpath)

        if background_image_divs:
            break
        else:
            time.sleep(.5)



    # 正则匹配 打乱了的图片的 url
    mathes = re.findall("background-image: url\(\"(.*)\"\);", background_image_divs[0].get_attribute('style'))
    imageurl = mathes[0]
    # 替换图片的后缀, ca58e81a.webp 变为 ca58e81a.jpg
    imageurl = imageurl.replace("webp", "jpg")

    location_list = []
    # 遍历52个DIV，获取它们的 position
    for background_image in background_image_divs:
        location={}

        #得出每个div的 x 和 y 坐标
        mathes = re.findall("background-position: (.*)px (.*)px;",background_image.get_attribute('style'))
        location['x']=int(mathes[0][0])
        location['y']=int(mathes[0][1])

        location_list.append(location)

    # 访问网络，得到图片
    jpg_file = io.BytesIO(urlopen(imageurl).read())

    #重新合并图片
    image = get_merge_image(jpg_file, location_list)

    return image

def is_similar(image1, image2, x, y):
    '''
    对比RGB值
    '''

    # 获得图片指定x和y的像素的 (r,g,b)
    pixel1=image1.getpixel((x, y))
    pixel2=image2.getpixel((x, y))

    for i in range(0,3):
        if abs(pixel1[i]-pixel2[i]) >= 55:
            return False

    return True

def get_diff_location(image1, image2):
    '''
    计算缺口的位置
    '''
    x = 0
    for x in range(0, 260):
        for y in range(0, 116):
            if not is_similar(image1, image2, x, y):
                return x