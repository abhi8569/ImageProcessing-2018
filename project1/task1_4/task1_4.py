import numpy as np
import numpy.fft as fft
from scipy.fftpack import fft2, ifft2, fftshift, ifftshift
from scipy import misc
import matplotlib.pyplot as plt

# task 1.4
# read the image
img_g = misc.imread("../img/bauckhage.jpg", mode='L') /255.
img_h = misc.imread("../img/clock.jpg", mode='L') /255.



# conduct fourier transformation G(x,y), H(x,y) and plot the result
fft_G = fft2(img_g)
fft_H = fft2(img_h)


print("Magnitude G", np.abs(fft_G))
print("Phase H", np.arctan(np.imag(fft_G)/np.real(fft_G)))

# Shift the origin to the center
misc.imsave("magnitude_G.png", fftshift(np.abs(fft_G)))
misc.imsave("phase_H.png", fftshift(np.arctan(np.imag(fft_G)/np.real(fft_G))))


# reconstruct image by the magnitude of G and the phse of H
magnitude = np.abs(fft_G)
phase =  1j * np.angle(fft_H)
fft_K = magnitude * np.exp(phase)


# conduct inverse fourier transform and plot the result
K = ifft2(fft_K)
plt.imshow(np.abs(K), cmap=plt.cm.gray)
plt.show()
misc.imsave("reconstructed.png", np.abs(K))



