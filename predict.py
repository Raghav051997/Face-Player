# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 11:27:22 2018

@author: Raghav Gandotra
"""

import cv2

fish=cv2.face.FisherFaceRecognizer_create()

fish.read('model.yml')
fish.predict()