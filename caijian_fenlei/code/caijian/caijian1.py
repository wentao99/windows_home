# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
 
img = Image.open('1.jpg') #打开当前路径图像
 
box1 = (14, 4, 53, 52)    #设置图像裁剪区域
 
image1 = img.crop(box1)   #图像裁剪
 
image1.save('image1.jpg')  #存储当前区域
