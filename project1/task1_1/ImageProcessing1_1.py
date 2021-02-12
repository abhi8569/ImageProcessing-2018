import numpy as np
import imageio as iio 

def image_mod(input_filename,rmin, rmax,output_filename):
    #------------------Arguments----------------------
    #input_filename : path for the input image
    #rmin : radius of inner bound
    #rmax : radius of outer bound
    #output_filename : path for the target image
    #------------------------------------------------- 
    g=iio.imread(input_filename) #reading and storing image in the form of nXm matrix

    new_image=np.zeros(shape=(np.shape(g))) #creating a placeholder for target image which has same size as that of input image
    
    w=np.shape(g)[0]/2          #coordinate of center
    h=np.shape(g)[1]/2          #of the image

    for x in np.arange(0,np.shape(g)[0]):            #iterating thgrough rows of the matrix
        for y in np.arange(0,np.shape(g)[1]):        #for each rows, iterate through columns
            distance=np.sqrt(np.power(x-w,2)+np.power(y-h,2)) #euclidean distance
            if distance>=rmin and distance<=rmax:       #condition to compute new image function
                new_image[x,y]=0
            else:
                new_image[x,y]=g[x,y]
        
    iio.imwrite(('%d_%d_'+output_filename) % (rmin,rmax),new_image) #write new image (appending rmin nad rmax in the image name)
    return

#Function call with different values of rmin and rmax

image_mod('clock.jpg',20,80,'clock_output.jpg')
image_mod('clock.jpg',100,120,'clock_output.jpg')
image_mod('clock.jpg',120,160,'clock_output.jpg')