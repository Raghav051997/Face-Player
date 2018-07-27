# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 19:34:10 2018

@author: Raghav Gandotra
"""

import numpy as np
from shutil import copyfile
import cv2
import glob

faceDet = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faceDet_two = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
faceDet_three = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faceDet_four = cv2.CascadeClassifier("haarcascade_frontalface_alt_tree.xml")
#define emotions as alist
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]

#def detect_faces(emotion):
def ten():
    files=glob.glob("new\\*") #get images from each of emotions one by one in file
    
    filenumber=0
    for f in files:
        frame=cv2.imread(f) #reading image 
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting images to gray scale
        
        #detect images using haarcascade filter
        face=faceDet.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10,minSize=(5,5),flags=cv2.CASCADE_SCALE_IMAGE)
        face_two=faceDet_two.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10,minSize=(5,5),flags=cv2.CASCADE_SCALE_IMAGE)
        face_three=faceDet_three.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10,minSize=(5,5),flags=cv2.CASCADE_SCALE_IMAGE)
        face_four=faceDet_four.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=10,minSize=(5,5),flags=cv2.CASCADE_SCALE_IMAGE)
        
        #now check if face is detected
        if len(face)==1:
            facefeatures=face
        elif len(face_two)==1:
            facefeatures=face_two
        elif len(face_three)==1:
            facefeatures=face_three
        elif len(face_four)==1:
            facefeatures=face_four
        else:
            facefeatures= ""
            
        #crop the image where x and y are axis and w and h are width and height of image
        for(x,y,w,h) in facefeatures:
            print ("face found in file: %s" %f)
            gray = gray[y:y+h,x:x+w]
            
            try:
                out=cv2.resize(gray,(350,350)) #resize image to all same size
                cv2.imwrite("new2\\e.jpg" ,out)
        
            except:
                pass
        filenumber += 1   #incrementing image number
  
#for emotion in emotions:
  #detect_faces(emotion) #calling function      
ten()               
                
                
        

