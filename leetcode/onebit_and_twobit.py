# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:25:25 2019

@author: Administrator
"""
def isOneBit(bits):
    i = 0
    while i < len(bits) - 1:
        if bits[i] == 1:
            i += 2
        else:
            i += 1
    if i == len(bits) - 1:
        return True
    else:
        return False
