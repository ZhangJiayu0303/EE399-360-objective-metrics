#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 12:24:51 2018

@author: zhangjiayu
"""

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_o=mpimg.imread('./bedroom.jpg')
img_c25 = mpimg.imread('./compressed pictures/compressedBedroom25.jpg')
img_c50 = mpimg.imread('./compressed pictures/compressedBedroom50.jpg')
img_c75 = mpimg.imread('./compressed pictures/compressedBedroom75.jpg')
img_c100 = mpimg.imread('./compressed pictures/compressedBedroom100.jpg')
reso = 4096

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


def ws_psnr(img_o, img_r, reso):
    
    wmse = 0
    size = img_o.shape
    dim1, dim2 = size[0], size[1]
    temp = np.ones((dim1, dim2))
    temp = temp * (np.arange(dim1).reshape(-1,1))
    sf = np.cos((temp - reso / 2.0 + 0.5) * (math.pi / reso))
#    (dim1, dim2) = img_o.shape
#    for i in range (0, dim1 - 1):
#        for j in range (0, dim2 - 1):
#            sf[i, j] = math.cos((j - reso/2 + 0.5) * (math.pi / reso))
    weight = sf / np.sum(sf)
#    for i in range (0, dim1 - 1):
#        for j in range (0, dim2 - 1):
    wmse = np.sum(weight * np.square(img_o - img_r))
#    print (wmse)            
    if abs(wmse) <= 0.00001: 
        return math.inf
    PIXEL_MAXIMUM = 255.0
#    print (wmse)
    return 10 * math.log10(PIXEL_MAXIMUM**2/wmse)

img_o = rgb2gray(img_o)
img_c25 = rgb2gray(img_c25)
img_c50 = rgb2gray(img_c50)
img_c75 = rgb2gray(img_c75)
img_c100 = rgb2gray(img_c100)


ws_psnr25 = ws_psnr(img_o, img_c25, reso)
ws_psnr50 = ws_psnr(img_o, img_c50, reso)
ws_psnr75 = ws_psnr(img_o, img_c75, reso)
ws_psnr100 = ws_psnr(img_o, img_c100, reso)

plt.plot([25, 50, 75, 100], [ws_psnr25,ws_psnr50,ws_psnr75,ws_psnr100], 'ro')
plt.ylabel('WS-PSNR values')
plt.xlabel('Compression Quality Factor')
for x, y in zip([25, 50, 75, 100], [ws_psnr25,ws_psnr50,ws_psnr75,ws_psnr100]):
    plt.text(x, y+0.3, '%.0f'%y, ha='center', va='bottom', fontsize=10.5)
plt.show()


