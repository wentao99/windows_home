# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:40:54 2018

@author: wentao99
"""
import os
import pandas as pd
import shutil

path = r'C:\Users\wentao99\Desktop'
os.chdir(path)
#读取文件并切分 pic1
f = open (r'C:\Users\wentao99\Desktop\挂件_label1_0706.txt')
file=pd.read_csv(f,header=None,sep=' ',encoding='gb2312')
file.drop([2],axis=1,inplace=True)
f.close()
#print(file)
file=file.reset_index(drop=True)
print(file)
pic=list(file.pop(0))#获得图片名
print(pic)
style=list(file.pop(1))#获得对应类型
print(style)

#转移图片
s0=0
s1=0
s2=0
s3=0
e=0
os.mkdir('0')#创建文件夹 有几个分类可以创建几个
os.mkdir('1')
os.mkdir('2')
os.mkdir('3')
path_img=r'C:\Users\wentao99\Desktop\st_0614'
for (dirpath,dirnames,ls) in os.walk(path_img):
    a=len(ls)
    print(ls)
    for i in ls:
        if i.endswith('.jpg'):
           
            if os.path.exists(path_img + '\\' + i):
                    print(path_img + '\\' + i)
                    
                    try:
                        x=pic.index(i)#找到图片i在pic所在的位置，则可以从对应的style中获得其类型
                        l=style[x]#该图片的类型
                        if l==0:
                            shutil.move(path_img + '\\'+ i, path +'\\0\\')
                            print(i+'转移到'+'0文件夹')
                            s0+=1
                        elif l==1:
                            print(path_img + '\\' + i)
                            print(path + '1\\')
                            shutil.move(path_img + '\\' + i, path +'\\1\\')
                            print(i+'转移到'+'1文件夹')
                            s1+=1
                        elif l==2:
                            shutil.move(path_img + '\\' + i, path +'\\2\\')
                            print(i+'转移到'+'2文件夹')
                            s2+=1
                        else:
                            shutil.move(path_img + '\\' + i, path +'\\3\\')
                            print(i+'转移到'+'3文件夹')
                            s3+=1
                    except:
                        e+=1
                        print('出现异常')
                        continue	
print("文件夹中共%d个文件，0文件内转移了%d个文件，1文件内转移了%d个文件，2文件内转移了%d个文件,出现的异常%d"%(a,s0,s1,s2,e))
