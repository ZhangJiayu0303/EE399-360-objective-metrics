#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:21:25 2018

@author: zhangjiayu
"""

import numpy
import math

def psnr(img1, img2):
    mse = numpy.mean((img1 - img2)**2)
    if mse == 0:
        return 10000
    PIXEL_MAXIMUM = 255.0
    return 20 *math.log10(PIXEL_MAXIMUM/math.sqrt(mse))
