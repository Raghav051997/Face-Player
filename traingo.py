# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:21:40 2018

@author: Raghav Gandotra
"""
#training and test set

import numpy as np
import cv2
import random
import glob
#initializing the classifier
fishface = cv2.face.FisherFaceRecognizer_create()
emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
data={}

#function split each emotion module (anger,neutral ,etc ) in training and test set of 80 and 20
def get_files(emotion):
    files=glob.glob("dataset\\%s\\*" %emotion)
    random.shuffle(files) #shuffle the data randomly
    training=files[:int(len(files)*0.8)]  #first 80% of file list(anger,disgust,etc) in training set
    prediction=files[-int(len(files)*0.2):] #last 20% in test set
    return training,prediction
def make_set():
    training_data=[]
    training_labels=[]
    prediction_data=[]
    prediction_labels=[]
    
    for emotion in emotions:
        training,prediction=get_files(emotion) #getting training and prediction(test) data for each module(anger,disgust etx)
        #put data in training and prediction(test ) list
        for item in training:
            image=cv2.imread(item)
            gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            training_data.append(gray)#appending gray image into training_data list
            training_labels.append(emotions.index(emotion))

        for item in prediction:
            image=cv2.imread(item)
            gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            prediction_data.append(gray) #put data to prediction(test )set
            prediction_labels.append(emotions.index(emotion))
            
    return training_data,training_labels,prediction_data,prediction_labels 
           
def run_recognizer():
   training_data,training_labels,prediction_data,prediction_label=make_set()
   print("training fisher_face classifier")
   print("size of traing set is:",len(training_labels),"images")
   fishface.train(training_data,np.asarray(training_labels))
   
   print("Predictin test set")
   cnt=0
   correct=0
   incorrect=0
   for image in prediction_data:
       pred,conf=fishface.predict(image)
       if pred==prediction_label[cnt]:
           correct+=1
           cnt+=1
       else:
           incorrect+=1
           cnt+=1
         
#run the recognizer
metascore=[]
for i in range(0,10):
   correct=run_recognizer()
   print("got"  ,correct,"percent correct")
   metascore.append(correct)


print ("\n\nend score:",np.mean(metascore),"percent correct!")            
           
        