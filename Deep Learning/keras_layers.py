#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 23:54:55 2019

@author: nj
"""

#model with simple hidden layer
import numpy as np
from keras.models import sequential
from keras.layers.core import Dense, Activation

#X - input training data
X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype = np.float32)

#y - output vector for each input vector
y = n.array([[0],[0],[0],[1]], dtype = np.float32)

#creating the sequential model
model = Sequential()

#adding input layer of 32 nodes with the same imput shape as training samples in x
model.add(Dense(32, input_dim = X.shape[1]))

#adding a softmax activation layer
model.add(Activation('softmax'))

#adding a fully connected output layer 
model.add(Dense(1))

#adding a sigmoid activation layer
model.add(Activation('sigmoid'))






