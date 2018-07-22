# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:49:16 2018

@author: wentao99
"""
from PIL import Image
 
img = Image.open(r'C:\Users\wentao99\Desktop\11111\P_20180302090035_810.jpg') #打开当前路径图像
 
box1 = (0, 0, 50, 100)    #设置图像裁剪区域
 
image1 = img.crop(box1)   #图像裁剪
 
image1.save(r'C:\Users\wentao99\Desktop\ceshi\P_20180302090035_810.jpg')  #存储当前区域

