# -*- coding: utf-8 -*-
from PIL import Image
import os
fin = 'C:\\Users\\wentao99\\Desktop\\1'
fout = 'C:\\Users\\wentao99\\Desktop\\test1' 
count = 0
for file in os.listdir(fin):
    if file.endswith('.jpg'):
        file_fullname = fin + '\\' +file
        img = Image.open(file_fullname)
#        img2 = img.copy
        a = [50, 0, 180, 100]
        box = (a)
        roi = img.crop(box)
        out_path = fout + '\\' + file[:-4] + '_1' +'.jpg'
        roi.save(out_path)
        count += 1
        print(count)
        
