import numpy as np
import matplotlib.pyplot as plt

def toFi(s,sigma):
    return np.exp(-0.5*(s/sigma)**2)
    
n = 20          #Number of sample points
sigma = 2       #variance
x = np.arange(n) + np.random.randn(n) * 0.2
y = np.random.rand(n) * 2

fis = np.zeros([n,n])
for i in range(0,n):
    for j in range(0,n):
        fis[i][j] = toFi(np.abs(x[i]-x[j]),sigma)
# fisInv = np.linalg.inv(np.matrix(fis))
# print(fisInv)
w = np.linalg.tensorsolve(fis, y)
print(w)

xs = np.linspace(0,n,200)
nfis = np.zeros([200,n])
for i in range(0,200):
    for j in range(0,n):
        nfis[i][j] = toFi(np.abs(xs[i]-x[j]),sigma)
ys = np.matmul(nfis,w)

plt.plot(x, y, 'o', label='Original data')
plt.plot(x,y)
plt.plot(xs, ys, 'g', label='Fitted line')
plt.ylim((-10,10))
plt.legend()
plt.show()