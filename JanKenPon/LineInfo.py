# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:20:40 2018

@author: Tanak
"""

import sys
import pygame
import pickle
import glob



aabbcc = 444

class LineInfo:
    def __init__(self, depth, x, y):
        self.depth = depth
        self.x = x
        self.y = y


def OutputData(name, list):
    with open(name, 'w') as f:
        pickle.dump(list, f)


def InputData(name):
    list = []
    with open(name,"rb") as f:
        list = pickle.load(f)

    return list