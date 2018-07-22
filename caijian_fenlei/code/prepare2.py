# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:40:54 2018

@author: 杨文韬
"""
import os
#import pandas as pd
import shutil
import random
os.chdir(r'F:\T')
path_img='F:\\T'
s0=0
s1=0
s2=0
s3=0
s4=0
r=random.sample(range(0,6000),600)#随机产生600个正整数，抽取出来后作为验证集
for (dirpath,dirnames,ls) in os.walk(path_img):
    a=len(ls)
    print(a)
#转移600个图片作为验证集，转移后将该图片的位置去掉
for y in r:
    if ls[y].endswith('.jpeg'):
        if os.path.exists(ls[y]):
            x=int(ls[y].split(".")[0].split("_")[-1])
            try:
                if os.path.exists(path_img+"\\val"):
                    shutil.move(path_img+'\\'+ls[y],'F:\\T\\val\\'+ls[y])
                    
                else:
                    os.mkdir("val")
                    shutil.move(path_img+'\\'+ls[y],'F:\\T\\val\\'+ls[y])
                f=open("val.txt",'a')
                f.write(ls[y]+' %d\n'%(x))
                f.close()
                print(ls[y]+'转移到'+'val文件夹')
                s4+=1
                del ls[y]
            except:
                print("转移测试集数据出现问题")
                
#转移图片进入训练数据集
os.mkdir("train")
for i in ls:
    if i.endswith('.jpeg'):
        if os.path.exists(i): 
            x=int(i.split(".")[0].split("_")[-1])
            try:
                if x == 0:
                    if os.path.exists(path_img+"\\train\\0"):
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\0\\'+i)
                    else:
                        os.mkdir(path_img+"\\train\\0")
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\0\\'+i)
                    f=open("train.txt",'a')
                    f.write("0/"+i+' 0\n')
                    f.close()
                    print(i+'转移到'+'0文件夹')
                    s0+=1
                elif x == 1:
                    if os.path.exists(path_img+"\\train\\1"):
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\1\\'+i)        
                    else:
                        os.mkdir(path_img+"\\train\\1")
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\1\\'+i)
                    f=open("train.txt",'a')
                    f.write("1/"+i+' 1\n')
                    f.close()
                    print(i+'转移到'+'0文件夹')
                    s1+=1
                elif x == 2:
                    if os.path.exists(path_img+"\\train\\2"):
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\2\\'+i)                            
                    else:
                        os.mkdir(path_img+"\\train\\2")
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\2\\'+i)
                    f=open("train.txt",'a')
                    f.write("2/"+i+' 2\n')
                    f.close()
                    print(i+'转移到'+'2文件夹')
                    s2+=1
                else:
                    if os.path.exists(path_img+"\\train\\3"):
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\3\\'+i)
                    else:
                        os.mkdir(path_img+"\\train\\3")
                        shutil.move(path_img+'\\'+i,'F:\\T\\train\\3\\'+i)
                    f=open("train.txt",'a')
                    f.write("3/"+i+' 3\n')
                    f.close()
                    print(i+'转移到'+'3文件夹')    
                    s3+=1
            except:
                print("转移训练集出现问题")
                continue
print("文件夹中共%d个文件，0文件内转移了%d个文件，1文件内转移了%d个文件，2文件内转移了%d个文件,转移到3文件夹的%d，转移到测试集文件夹共%d"%(s0+s1+s2,s0,s1,s2,s3,s4))