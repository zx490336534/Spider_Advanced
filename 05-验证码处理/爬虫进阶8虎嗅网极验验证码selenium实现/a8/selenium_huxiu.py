#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Terry'

import random

import time
from selenium.webdriver import ActionChains

from a8.img_handle import get_image, get_diff_location


from selenium import webdriver

class GeettestHuXiu(object):

    def __init__(self):
        self.__create_driver()

    # 启动selenium
    def __create_driver(self):
        driver = webdriver.Firefox()
        driver.set_page_load_timeout(10)
        driver.set_script_timeout(10)
        driver.set_window_size(1366, 768)
        self.driver = driver

    def __quit_driver(self):
        if self.driver:
            self.driver.quit()

    def visit(self):
        # 访问虎嗅网首页
        url = 'https://www.huxiu.com/'
        self.driver.get(url)

        # 找到 注册按钮
        reg = self.driver.find_element_by_xpath('/html/body/header/div/ul[2]/li[4]/a')
        # 点击注册按钮
        reg.click()

        time.sleep(.5)

        # 得到有缺口的 打乱了的图片
        image1 = get_image(self.driver, "//div[@class='gt_cut_bg gt_show']/div")
        # 得到完整的  打乱了的图片
        image2 = get_image(self.driver, "//div[@class='gt_cut_fullbg gt_show']/div")

        # 计算缺口位置的x坐标
        loc_x = get_diff_location(image1, image2)


        self.move(loc_x)

    # 移动鼠标，移动的距离为 loc_x
    def move(self, loc_x):
        # 生成x的移动轨迹点
        track_list = self.get_track(loc_x)

        #     找到滑动模块
        ele_slider = self.driver.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")
        location = ele_slider.location
        #     获得滑动模块的高度
        y = location['y']

        #     鼠标点击元素并按住不放
        ActionChains(self.driver).click_and_hold(on_element=ele_slider).perform()
        time.sleep(0.15)

        # 进行模拟的鼠标移动
        # 22是估计缺口图片宽度的一半
        for track in track_list:
            y_offset = random.randint(100, 110)
            ActionChains(self.driver).move_to_element_with_offset(to_element=ele_slider, xoffset=track + 22,
                                                             yoffset=y - y_offset).perform()
            #    间隔时间也通过随机函数来获得
            time.sleep(random.randint(10, 30) / 100)

        # 缺口图片往前多移动了一些，需要往后移动一些距离
        i  = int(loc_x / 5) # 误差的值，回退几步，未完成
        for _ in range(5):
            y_offset = random.randint(100, 110)
            ActionChains(self.driver).move_to_element_with_offset(to_element=ele_slider, xoffset=21, yoffset=y - y_offset).perform()
            time.sleep(0.1)

        #   释放鼠标
        ActionChains(self.driver).release(on_element=ele_slider).perform()

        time.sleep(3)

        # 退出
        # self.__quit_driver()

    def get_track(self, length):
        '''
        根据缺口的位置模拟x轴移动的轨迹
        '''
        list = []

        # 移动的距离 通过随机范围函数来获得
        x = random.randint(2, 4)
        while length - x >= 5:
            list.append(x)

            length = length - x
            x = random.randint(2, 4)

        # length中，剩下的长度，都每次移动 1 像素点
        for i in range(length):
            list.append(1)

        return list

if __name__ == '__main__':
    geettestHuXiu = GeettestHuXiu()
    geettestHuXiu.visit()



