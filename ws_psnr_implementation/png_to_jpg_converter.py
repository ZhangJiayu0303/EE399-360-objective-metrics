#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:42:42 2018

@author: zhangjiayu
"""

from PIL import Image
im = Image.open("./bedroom.png")
im = im.convert('RGB')
im.save('bedroom.jpg', quality=100)

im = Image.open("./seaside.png")
im = im.convert('RGB')
im.save('seaside.jpg', quality=100)

im = Image.open("./livingroom.png")
im = im.convert('RGB')
im.save('livingroom.jpg', quality=100)