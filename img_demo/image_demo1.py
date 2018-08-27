#coding=utf-8
'''
Created on 2018年5月4日

@author: yongmao.wu
'''
 
from PIL import Image
import pytesseract  
i=Image.open("F:\\img\\test.jpg")
print(i.size)
#上面都是导包，只需要下面这一行就能实现图片文字识别
 
# print(text) 
  