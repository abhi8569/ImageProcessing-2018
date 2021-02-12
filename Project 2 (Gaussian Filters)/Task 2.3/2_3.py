#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 18:46:57 2018

@author: shahnawaz
"""

import numpy as np
import scipy.misc as msc

for name in ['clock','bauckhage']:   #Images to be filtered
    for sd in np.arange(0,10):      #Varying standard deviation from 0 to 9
        # Evaluation of filter response parameters
        a1=1.6800   
        a2=-0.6803
        b1=3.7350
        b2=-0.2598
        c1=1.7830
        c2=1.7230
        d1=0.6318
        d2=1.9970
        e=np.pi
        
        a0p=a1+a2
        a1p=(np.power(e,-1*c2/sd)*(b2*np.sin(d2/sd)-((a2+(2*a1))*np.cos(d2/sd))))+((np.power(e,-1*c1/sd))*(b1*np.sin(d1/sd)-((a1+(2*a2))*np.cos(d1/sd))))
        a2p=(2*np.power(e,-1*(c1+c2)/sd)*((a1+a2)*np.cos(d2/sd)*np.cos(d1/sd)-np.cos(d2/sd)*b1*np.sin(d1/sd)-np.sin(d2/sd)*b2*np.cos(d1/sd)))+(a2*np.power(e,-2*c1/sd))+(a1*np.power(e,-2*c2/sd))
        a3p=(np.power(e,-1*(c2+(2*c1))/sd)*(b2*np.sin(d2/sd)-a2*np.cos(d2/sd)))+(np.power(e,-1*(c1+(2*c2))/sd)*(b1*np.sin(d1/sd)-a1*np.cos(d1/sd)))
        
        b1p=-(2*np.power(e,-1*c2/sd)*np.cos(d2/sd))-(2*np.power(e,-1*c1/sd)*np.cos(d1/sd))
        b2p=(4*np.cos(d2/sd)*np.cos(d1/sd)*np.power(e,-1*(c1+c2)/sd))+np.power(e,-2*c2/sd)+np.power(e,-2*c1/sd)
        b3p=(-2*np.cos(d1/sd)*np.power(e,-1*(c1+(2*c2))/sd))-(2*np.cos(d2/sd)*np.power(e,-1*(c2+(2*c1))/sd))
        b4p=np.power(e,-2*(c1+c2)/sd)
        
        b1m=b1p
        b2m=b2p
        b3m=b3p
        b4m=b4p
        	
        a1m=a1p-b1p*a0p
        a2m=a2p-b2p*a0p
        a3m=a3p-b3p*a0p
        a4m=-1*b4p*a0p
        
        # Reading the image
        img=msc.imread('../img/'+name+'.jpg',flatten=True)
        img_1st = 255*np.ones_like(img) # For storing Causal component of recursive filtering
        img_2nd = 255*np.ones_like(img) # For storing Anti-Causal component of recursive filtering
        img_final = np.copy(img)    # For storing filtered signal in recursive filtering
        
        for y in np.arange(0,np.shape(img)[1]):
            for x in np.arange(0,np.shape(img)[0]): 
                if x>3 and x<(np.shape(img)[0]-4):
                    img_1st[x][y] = (a0p*img[x-0][y]+a1p*img[x-1][y]+a2p*img[x-2][y]+a3p*img[x-3][y])-(b1p*img_1st[x-1][y]+b2p*img_1st[x-2][y]+b3p*img_1st[x-3][y]+b4p*img_1st[x-4][y]) # For Causal
                    img_2nd[x][y] = (a1m*img[x+1][y]+a2m*img[x+2][y]+a3m*img[x+3][y]+a4m*img[x+4][y])-(b1m*img_2nd[x+1][y]+b2m*img_2nd[x+2][y]+b3m*img_2nd[x+3][y]+b4m*img_2nd[x+4][y]) # For Anti-Causal
        img_final = img_1st + img_2nd
        img_final*=(1/(sd*np.sqrt(2*np.pi)))
        
        img_1st = 255*np.ones_like(img) # For storing Causal component of recursive filtering
        img_2nd = 255*np.ones_like(img) # For storing Anti-Causal component of recursive filtering

        
        for x in np.arange(0,np.shape(img_final)[0]):
            for y in np.arange(0,np.shape(img_final)[1]):
                if y>3 and y<(np.shape(img_final)[1]-4):
                    img_1st[x][y] = (a0p*img_final[x][y-0]+a1p*img_final[x][y-1]+a2p*img_final[x][y-2]+a3p*img_final[x][y-3])-(b1p*img_1st[x][y-1]+b2p*img_1st[x][y-2]+b3p*img_1st[x][y-3]+b4p*img_1st[x][y-4]) # For Causal
                    img_2nd[x][y] = (a1m*img_final[x][y+1]+a2m*img_final[x][y+2]+a3m*img_final[x][y+3]+a4m*img_final[x][y+4])-(b1m*img_2nd[x][y+1]+b2m*img_2nd[x][y+2]+b3m*img_2nd[x][y+3]+b4m*img_2nd[x][y+4]) # For Anti-Causal
        
        img_final = img_1st + img_2nd
        img_final*=(1/(sd*np.sqrt(2*np.pi)))
        
        msc.toimage(img_final).save(name+'Filtered_sigma='+str(sd)+'.jpg') # Saving filtered image 
    msc.toimage(img).save(name+'Original.jpg')  # Original Image 
           
            
            
        
