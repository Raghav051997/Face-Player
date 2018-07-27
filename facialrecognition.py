# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:32:05 2018

@author: Raghav Gandotra
"""
    
import glob
from shutil import copyfile
import cv2

emotions=["neutral","anger","contempt","disgust","fear","happy","sadness","surprise"]#define emotion order
participants=glob.glob("source_emotion\\*")

for x in participants:
    part="%s" %x[-4:]
    for sessions in glob.glob("%s\\*"%x):
     for files in glob.glob("%s\\*" %sessions):
         current_session=files[20:-30]
         file=open(files,'r')
         
         emotion=int(float(file.readline()))
         
         sourcefile_emotion = glob.glob("source_images\\%s\\%s\\*" %(part, current_session))[-1] #get path for last image in sequence, which contains the emotion
         sourcefile_neutral = glob.glob("source_images\\%s\\%s\\*" %(part, current_session))[0] #do same for neutral image
            
         dest_neut = "sorted_set\\neutral\\%s" %sourcefile_neutral[25:] #Generate path to put neutral image
         dest_emot = "sorted_set\\%s\\%s" %(emotions[emotion], sourcefile_emotion[25:]) #Do same for emotion containing image
            
         copyfile(sourcefile_neutral, dest_neut) #Copy file
         copyfile(sourcefile_emotion, dest_emot) #Copy file

 

