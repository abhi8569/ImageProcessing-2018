#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 00:05:02 2019

@author: shahnawaz
"""

import numpy as np
import scipy.misc as msc

isle_img=msc.imread('../img/isle.jpg',flatten=True)
clock_img=msc.imread('../img/clock.jpg',flatten=True)

U = np.shape(clock_img)[0]
V = np.shape(clock_img)[1]

X = np.array([[215, 365, 218, 364], 
               [56, 10, 258, 296]])
UV = np.array([[0, V, 0, V], 
               [0, 0, U, U]])

Matrix = np.zeros([8,8]);
Matrix[0:np.shape(UV)[1],0:np.shape(UV)[0]+1] = np.array(np.concatenate((np.transpose(UV),np.ones([4,1])),1))
Matrix[np.shape(UV)[1]:2*np.shape(UV)[1],np.shape(UV)[0]+1:2*(np.shape(UV)[0]+1)] = np.array(np.concatenate((np.transpose(UV),np.ones([4,1])),1))
Matrix[:,6:7] =-1*np.multiply(np.reshape(X,[8,1]),np.reshape(np.concatenate((UV[0,:],UV[0,:])),[8,1]))
Matrix[:,7:8] =-1*np.multiply(np.reshape(X,[8,1]),np.reshape(np.concatenate((UV[1,:],UV[1,:])),[8,1]))

[[a],[b],[c],[d],[e],[f],[g],[h]] = np.dot(np.linalg.inv(Matrix),np.reshape(X,[8,1]))

for i in range(0,U):
    for j in range(0,V):
        x = (a*i+b*j+c)/(g*i+h*j+1)
        y = (d*i+e*j+f)/(g*i+h*j+1)
        isle_img[int(y),int(x)]=clock_img[j,i];
        
msc.toimage(isle_img).save('output.jpg')
        