# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:28:39 2018

@author: NikhilJain
"""
import numpy as np

def cross_entropy(Y,P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1-Y)*np.log(1-P))
