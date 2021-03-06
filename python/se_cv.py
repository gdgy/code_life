#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 18:47
# @Author  : shaoyong_li
# @Site    : 
# @File    : se_cv.py
# coding:utf-8
import cv2
import sys
reload(sys)
sys.setdefaultencoding('utf8')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(1, 10.0)
#此处fourcc的在MAC上有效，如果视频保存为空，那么可以改一下这个参数试试, 也可以是-1
fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
# 第三个参数则是镜头快慢的，10为正常，小于10为慢镜头
out = cv2.VideoWriter('/opt/code/video/output2.avi', fourcc,10,(640,480))
while True:
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
        a = out.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()

# 拍照
import cv2

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("/opt/code/image/fangjian2.jpeg", frame)
        break
cap.release()
cv2.destroyAllWindows()