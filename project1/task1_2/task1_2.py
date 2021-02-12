"""
Author: Yung-Yu Chen

"""
import numpy as np
import numpy.fft as fft
from scipy.fftpack import fft2, ifft2, fftshift, ifftshift
from scipy import misc
import matplotlib.pyplot as plt


# task 1.2
n = 512
x = np.linspace(0, 2*np.pi, n)
f = np.sin(x)

plt.plot(x, f, "k-")
plt.show()

F = fft.fft(f)

w = fft.fftfreq(n)
plt.plot(w, np.abs(F), "k-")
plt.show()

plt.plot(w, np.log(np.abs(F)), 'k-')
plt.show()
# Init the parameters
offset = 1.
amplitude = -2.
frequency = 16.
phase = np.pi

# Varying the offset and plot them
fig = plt.figure(1)
i = 0
for offset in [1., 2, 4, 8]:
    f = offset + amplitude * np.sin(frequency*x + phase)
    F = fft.fft(f)
    F = fft.fftshift(F)
    sub = fig.add_subplot(2,2,i+1)
    sub.set_title("offset:{}".format(offset))
    sub.plot(np.abs(F), 'k-')    
    i=i+1
plt.tight_layout()
plt.show()
fig.savefig("offset.png")

# Varying the amplitude and plot them
fig = plt.figure(1)
i = 0
for amplitude in [-2, 2]:
    f = offset + amplitude * np.sin(frequency*x + phase)
    F = fft.fft(f)
    F = fft.fftshift(F)
    sub = fig.add_subplot(1,2,i+1)
    sub.set_title("amplitude:{}".format(amplitude))
    sub.plot(np.abs(F), 'k-')    
    i=i+1
plt.tight_layout()
plt.show()
fig.savefig("amplitude.png")

# Varying the frequency and plot them
fig = plt.figure(1)
i = 0
for frequency in [1, 8, 16, 64]:
    f = offset + amplitude * np.sin(frequency*x + phase)
    F = fft.fft(f)
    F = fft.fftshift(F)
    sub = fig.add_subplot(2,2,i+1)
    sub.set_title("frequency:{}".format(frequency))
    sub.plot(np.abs(F), 'k-')    
    i=i+1
plt.tight_layout()
plt.show()
fig.savefig("frequency.png")

# Varying the amplitude and plot them
fig = plt.figure(1)
i = 0
for phase in [0, np.pi, 2*np.pi]:
    f = offset + amplitude * np.sin(frequency*x + phase)
    F = fft.fft(f)
    F = fft.fftshift(F)
    
    sub = fig.add_subplot(1,3,i+1)
    sub.set_title("phase:{}".format(phase))
    sub.plot(np.abs(F), 'k-')    
    i=i+1
plt.tight_layout()
plt.show()    
fig.savefig("phase.png")