#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import imageio as imo
import scipy.ndimage as img

def toBiSinSpace(f,ampx,vx,phix,ampy,vy,phiy):
    rows,cols = f.shape
    
    # make a new numpy array depends on rows and columns of first image and amplitude that will be choosen
    # rows+(2*amp) evenly spaced samples, calculated over the interval [ -amplitude, rows+amplitude] 
    
    x,y = np.meshgrid(np.linspace(-ampx,cols+ampx,cols+(2*ampx)),
                       np.linspace(-ampy,rows+ampy,rows+(2*ampy)))
    # wave function
    xs,ys = x+ampx*np.sin(2*np.pi*(y/cols)*vx + phix),y+ampy*np.sin(2*np.pi*(x/rows)*vy + phiy)
    
    xs,ys = xs.reshape(-1),ys.reshape(-1)
    
    coords = np.vstack((ys,xs))
    
    #Map the input array to new coordinates by interpolation
    g = img.map_coordinates(f,coords, order = 3)
    
    # change the shape of new imgage 
    h = g.reshape(rows+2*ampy,cols+2*ampx)
    
    return h

f = imo.imread('clock.jpg')

out1_01=toBiSinSpace(f,0,0,0,128,0.5,0) # Vertical amplitude = 128, frequency = 1/2, phase = 0
imo.imwrite('Picture 1_01.jpg',out1_01)


out1_1=toBiSinSpace(f,0,0,0,128,0.5,np.pi) # Vertical amplitude = 128, frequency = 1/2, phase = pi
imo.imwrite('Picture 1_1.jpg',out1_1)

#######################################################################

out2_01=toBiSinSpace(f,0,0,0,128,1,0) # Vertical amplitude = 128, frequency = 1, phase = 0
imo.imwrite('Picture 2_01.jpg',out2_01)

out2_1=toBiSinSpace(f,0,0,0,128,1,np.pi/2) # Vertical amplitude = -128, frequency = 1, phase = pi/2
imo.imwrite('Picture 2_1.jpg',out2_1)

#############################################################


out3_01 = toBiSinSpace(f,10,2,-np.pi/4,10,2,-np.pi/2) # Both Horizontal and Vertical
imo.imwrite('Picture 3_01.jpg',out3_01)


out3_1 = toBiSinSpace(f,10,2,-np.pi/2,10,2,-np.pi/2) # Both Horizontal and Vertical
imo.imwrite('Picture 3_1.jpg',out3_1)

out3_2 = toBiSinSpace(f,20,2,-np.pi/4,10,2,-np.pi/2) # Both Horizontal and Vertical
imo.imwrite('Picture 3_2.jpg',out3_2)

out3_3 = toBiSinSpace(f,10,4,-np.pi/4,10,2,-np.pi/2) # Both Horizontal and Vertical
imo.imwrite('Picture 3_3.jpg',out3_3)


######################################################

# first, Implement vertical
# second, Implement horizontal on the result of frist step

out4_01=toBiSinSpace(f,0,0,0,6,5,0) 
imo.imwrite('picture 4_01.jpg',out4_01)
out4_02=toBiSinSpace(out4_01,15,5,-np.pi/6,0,0,0) 
imo.imwrite('picture 4_02.jpg',out4_02)

# just for see the result of little change

out4_1=toBiSinSpace(f,0,0,0,6,5,0)
imo.imwrite('picture 4_1.jpg',out4_1)
out4_2=toBiSinSpace(out4_1,10,5,-np.pi/6,0,0,0)
imo.imwrite('picture 4_2.jpg',out4_2)


out4_3=toBiSinSpace(out4_1,15,7,-np.pi/6,0,0,0)
imo.imwrite('picture 4_3.jpg',out4_3)


#########################################################

# first, Implement vertical
# second, Implement horizontal on the result of frist step


out5_01 = toBiSinSpace(f,0,0,0,10,8,0) 
imo.imwrite('Picture 5_01.jpg',out5_01)
out5_02 = toBiSinSpace(out5_01,10,1.15,np.pi*3/4,0,0,0)  
imo.imwrite('Picture 5_02.jpg',out5_02)


out5_1 = toBiSinSpace(f,0,0,0,10,4,0) 
imo.imwrite('Picture 5_1.jpg',out5_1)
out5_2 = toBiSinSpace(out5_1,20,1.15,np.pi*3/4,0,0,0)  
imo.imwrite('Picture 5_2.jpg',out5_2)



# In[ ]:





# In[ ]:




