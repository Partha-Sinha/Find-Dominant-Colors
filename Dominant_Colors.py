#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:40:52 2019

@author: Partha Pratim Sinha
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.cluster import KMeans

def rgb2hex(rgb):
    hex = "#{:02x}{:02x}{:02x}".format(int(rgb[0]), int(rgb[1]), int(rgb[2]))
    return hex


img = cv2.imread('/home/zeref/Find-Dominant-Colors/1.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_neutral = np.array([11,20,40])       
upper_neutral = np.array([180,250,250])
mask = cv2.inRange(hsv, lower_neutral, upper_neutral)
img = cv2.bitwise_and(img,img, mask = mask)
img = img.reshape((img.shape[0] * img.shape[1],3))

clt = KMeans(n_clusters=5)
labels = clt.fit_predict(img)
label_counts = Counter(labels)
total_count = sum(label_counts.values())
        
center_colors = list(clt.cluster_centers_)
ordered_colors = [center_colors[i]/255 for i in label_counts.keys()]
color_labels = [rgb2hex(ordered_colors[i]*255) for i in label_counts.keys()]
        

plt.figure(figsize=(14, 8))
plt.subplot(221)
plt.imshow(img_rgb)
plt.axis('off')
        
plt.subplot(222)
plt.pie(label_counts.values(),labels=color_labels, colors=ordered_colors, startangle=90, shadow=1, autopct='%1.1f%%')
plt.axis('equal')
plt.xlabel('Note: Black color on histogram represents neutral colors')
plt.show()
