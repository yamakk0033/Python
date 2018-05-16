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


def DrawLines(screen, array):
    buff = []
    for info in array:
        buff.append((info.x, info.y))

    if len(buff) > 1:
        print("aa")
        pygame.draw.lines(screen, (255, 255, 255), False, buff)
    elif len(buff) == 1:
        print("bb")
        pygame.draw.circle(screen, (255, 255, 255), buff[0], 5)


def DrawLinesEx(screen, array):
    prev = 0
    buff = []

    for info in array:
        if info.depth != prev:
            DrawLines(screen, buff)
            buff = []
        buff.append(info)
        prev = info.depth

    DrawLines(screen, buff)



def OutputData(name, list):
    with open(name, 'w') as f:
        pickle.dump(list, f)


def InputData(name):
    list = []
    with open(name,"rb") as f:
        list = pickle.load(f)

    return list



def GetFiles(name):
    return glob.glob(name)





