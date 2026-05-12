import numpy as np
import math as m
class square():
    def __init__(self, side,posx,posy):
        self.side=side
        self.area=side*side
        self.center = [posx,posy]
class circle():
    def __init__(self, radie,posx,posy):
        self.radie = radie
        self.center = [posx,posy]

class runloop():
    def __init__(self):
        self.time = 0
        self.figures = []
    def addfigure(self,figure):
        self.time +=1
        self.figures.append(figure)

        



def plane(lenth, figures):
    