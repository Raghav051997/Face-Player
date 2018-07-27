# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:31:09 2018

@author: Raghav Gandotra
"""

import cv2
import glob
import random
import numpy as np
from requests import get 
fish =cv2.face.FisherFaceRecognizer_create()
fish.read('model.yml')
a=cv2.imread('new2\\e.jpg')
gray=cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
result,conf=fish.predict(gray);
if result==0:
    genreNo='country'
    
elif result==1:
    genreNo='metal'
elif result==2:
    genreNo='hiphop'    
elif result==3:
    genreNo='randb'
elif result==4:
    genreNo='folk'    
elif result==5:
    genreNo='blues'    
elif result==6:
    genreNo='jazz'          
elif result==7:
    genreNo='latin'              
url='http://musicovery.com/api/V5/playlist.php?&fct=getfromlocation&location=india&resultsnumber=25&genreNo="'+genreNo+'" &format=json'    
dic=get(url)    
data=dic.json()
data=data['root']['tracks']['track']
k=[]
for i in data:
    k.append(i['title'])
    