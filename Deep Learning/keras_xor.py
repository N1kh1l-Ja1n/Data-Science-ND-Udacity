#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 00:20:14 2019

@author: nj
"""

#Building a simple multi layer feedforward neuarl network to solve XOR problem
import numpy as np
from keras.utils import np_utils
import tensorflow as tf
# Using TensorFlow 1.0.0; use tf.python_io in later versions
tf.python.control_flow_ops = tf

# Set random seed
np.random.seed(42)

# Our data
X = np.array([[0,0],[0,1],[1,0],[1,1]]).astype('float32')
y = np.array([[0],[1],[1],[0]]).astype('float32')

# Initial Setup for Keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation
# One-hot encoding the output
y = np_utils.to_categorical(y)

# Building the model
xor = Sequential()

# Add required layers
xor.add(Dense(32, input_dim = 2))
xor.add(Activation('tanh'))
xor.add(Dense(2))
xor.add(Activation('softmax'))


# Specify loss as "binary_crossentropy", optimizer as "adam",
# and add the accuracy metric
xor.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])

xor.summary()

# Fitting the model
history = xor.fit(X, y, nb_epoch=900, verbose=0)

# Scoring the model
score = xor.evaluate(X, y)
print("\nAccuracy: ", score[-1])

# Checking the predictions
print("\nPredictions:")
print(xor.predict_proba(X))