import numpy as np
import scipy.misc as msc
import numpy.fft as fft

img=msc.imread('../img/clock.jpg',flatten=True) 

# apply fourier transform
fourier_image=fft.fft2(img)
msc.toimage(np.log10(np.abs(fourier_image))).save('step1_fourier.jpg')
# fourier shift the frequency matrix 
f_shifted_log = np.log10(np.abs(fft.fftshift(fourier_image)))
f_shifted = fft.fftshift(fourier_image)
# save the shifted fft matrix by logarithm
msc.toimage(f_shifted_log).save('step2_fourier_shifted.jpg')

# define band min and max
rmin=10
rmax=50
w=np.shape(f_shifted)[0]/2
h=np.shape(f_shifted)[1]/2

# Filtering: suppress the value outside of the band
filtered_image=np.zeros(shape=(np.shape(f_shifted)))
for x in np.arange(0,np.shape(f_shifted)[0]):
    for y in np.arange(0,np.shape(f_shifted)[1]):
        distance=np.sqrt(np.power(x-w,2)+np.power(y-h,2))
        if distance>=rmin and distance<=rmax:
            f_shifted[x,y]=f_shifted[x,y]
        else:
            f_shifted[x,y]=1

msc.toimage(np.log10(np.abs(f_shifted))).save('step3_filtered.jpg')

# invere fft shifting
inverse_fftshift=fft.ifftshift(f_shifted)
msc.toimage(np.log10(np.abs(inverse_fftshift))).save('step4_inverse_fftshifted.jpg')
# inverse fft
inverse_fourier=fft.ifft2(inverse_fftshift)
msc.toimage(np.abs(inverse_fourier)).save('step5_inverse_fourier.jpg')