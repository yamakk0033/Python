# -*- coding: utf-8 -*-
"""
Created on Tue May 15 21:20:40 2018

@author: Tanak
"""

import pygame
import pickle
import glob



class LineInfo:
    def __init__(self, depth, x, y):
        self.depth = depth
        self.x = x
        self.y = y


def DrawLines(screen, color, array):
    buff = []
    for info in array:
        buff.append((info.x, info.y))

    if len(buff) > 1:
        pygame.draw.lines(screen, color, False, buff, 2)
#        for aaa in buff:
#            pygame.draw.circle(screen, color, aaa, 3)
            
    elif len(buff) == 1:
        pygame.draw.circle(screen, color, buff[0], 2)


def DrawLinesEx(screen, color, array, limit = -1):
    prev = 0
    buff = []
    
    counter = 0

    for info in array:
        if limit >= 0 and counter >= limit:
            break
        if info.depth != prev:
            DrawLines(screen, color, buff)
            buff = []
        buff.append(info)
        
        prev = info.depth
        counter += 1

    DrawLines(screen, color, buff)



def OutputData(name, array):
    with open(name, 'wb') as f:
        pickle.dump(array, f)


def InputData(name):
    array = []
    with open(name,"rb") as f:
        array = pickle.load(f)

    return array



def GetFiles(name):
    return glob.glob(name)





