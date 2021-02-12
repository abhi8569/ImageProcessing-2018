import numpy as np
import scipy.ndimage as img
import scipy.misc



image = img.imread('./clock.jpg').astype(np.float32)
def xy2rphi(x, y):
    r   = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return r, phi

def rphi2xy(r, phi):
    
    x = r*np.cos(phi)
    y = r*np.sin(phi)
    
    return x, y

def extenstion_from_r_phi_plane(g, m, n, rmax, phimax, rmin):
    xs, ys = np.meshgrid(np.arange(n) - n/2, np.arange(m) - m/2, sparse=True)
    rs, phis =xy2rphi(xs, ys)
    rs, phis = rs.reshape(-1), phis.reshape(-1)

    phis = phis + np.pi
    rs = rs - rmin # task3.3-2
    
    iis = phis/phimax*(m-1) 
    jjs = rs /rmax*(n-1) 
    coords = np.vstack((iis, jjs))
    
    h = img.map_coordinates(g, coords, order=3)
    h = h.reshape(m, n)
    return np.flipud(h)


f = image
f = np.flipud(f)
f = np.rot90(f)
m, n   = f.shape
rmax   = n/2
phimax = np.pi * 2
img_name = "clock"
g = extenstion_from_r_phi_plane(f, m, n, rmax, phimax, 0)
scipy.misc.imsave('{}_1.jpg'.format(img_name), g)
h = extenstion_from_r_phi_plane(f, m, n, rmax, phimax, 10)
scipy.misc.imsave('{}_2.jpg'.format(img_name), h)

