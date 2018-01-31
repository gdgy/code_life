#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/16 11:57
# @Author  : shaoyong_li
# @Site    : 
# @File    : tiao.py
import math
import os
import tempfile
import time
from functools import reduce
from PIL import Image
BACKGROUND_POS = (40, 500)
DISTANCE_TO_TIME_RATIO = 1.35
SCREENSHOT_PATH = tempfile.gettempdir() + "/screenshot.png"


def calculate_jump_distance():
    im = Image.open(SCREENSHOT_PATH)
    background_rgb = im.getpixel(BACKGROUND_POS)
    role_pos_list = None
    vertex1_pos = None
    block_background_rgb = None
    vertex2_pos = None
    role_line_flag = True
    for y in range(BACKGROUND_POS[1], im.height):
        if role_pos_list and role_line_flag:
            break
        role_line_flag = True
        vertex2_line_flag = True
        for x in range(BACKGROUND_POS[0], im.width):
            current_rgb = im.getpixel((x, y))
            next_rgb = im.getpixel((x + 1, y)) if x + 1 < im.width else (0, 0, 0)
            # 识别顶点1
            if x > BACKGROUND_POS[0] and y > BACKGROUND_POS[1] and not vertex1_pos \
                    and not is_similar(background_rgb, current_rgb) and is_similar(current_rgb, next_rgb):
                vertex1_pos = (x, y)
                block_background_rgb = current_rgb
            # 识别顶点2
            if block_background_rgb and vertex2_line_flag and is_similar(current_rgb, block_background_rgb, 5):
                vertex2_line_flag = False
                if vertex2_pos:
                    if x < vertex2_pos[0] and vertex2_pos[0] - x < 20 and y - vertex2_pos[1] < 20:
                        vertex2_pos = (x, y)
                else:
                    vertex2_pos = (x, y)
            # 识别小人
            if is_part_of_role(current_rgb):
                if role_line_flag:
                    role_pos_list = []
                    role_line_flag = False
                role_pos_list.append((x, y))
    if len(role_pos_list) == 0:
        raise Exception('无法识别小人位置！！！')
    pos_sum = reduce((lambda o1, o2: (o1[0] + o2[0], o1[1] + o2[1])), role_pos_list)
    role_pos = (int(pos_sum[0] / len(role_pos_list)), int(pos_sum[1] / len(role_pos_list)))
    destination_pos = (vertex1_pos[0], vertex2_pos[1])
    return int(linear_distance(role_pos, destination_pos))


def is_part_of_role(rgb):
    return 53 < rgb[0] < 59 and 57 < rgb[1] < 61 and 95 < rgb[2] < 103


def linear_distance(xy1, xy2):
    return math.sqrt(pow(xy1[0] - xy2[0], 2) + pow(xy1[1] - xy2[1], 2))


def is_similar(rgb1, rgb2, degree=10):
    return abs(rgb1[0] - rgb2[0]) <= degree and abs(rgb1[1] - rgb2[1]) <= degree and abs(rgb1[2] - rgb2[2]) <= degree


def screenshot():
    os.system("adb shell screencap -p /mnt/sdcard/screencap.png")
    os.system("adb pull /mnt/sdcard/screencap.png {} >> {}/jump.out".format(SCREENSHOT_PATH, tempfile.gettempdir()))


def jump(touch_time):
    os.system("adb shell input swipe 0 0 0 0 {}".format(touch_time))


def distance2time(distance):
    return int(distance * DISTANCE_TO_TIME_RATIO)


if __name__ == '__main__':
    count = 1
    while True:
        screenshot()
        distance = calculate_jump_distance()
        touch_time = distance2time(distance)
        jump(touch_time)
        print("#{}: distance={}, time={}".format(count, distance, touch_time))
        count += 1
        time.sleep(1)