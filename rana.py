import math
import os 
import random
import re
import sys 
class Coordenadas:
    def __int__ (self, x,y):
        self.x = x
        self.y = y
    def comparate (self,x,y):
        if self.x == x and self.y == y:
            return True
        else: 
            return False

class Tunel:
    def __init__(self,x1,x2,y1,y2):
        self.extremo1 = Coordenadas(x1,y1)
        self.extremo2 = Coordenadas (x2,y2)

def BuscaTunel (casillax, casillay, tuneles):
    coordenadas = Coordenadas(casillax, casillay)
    for t in tuneles:
        if t.extremo1.comparate(casillax,casillay)==True:
            coordenadas.x = t.extremo2.x
            coordenadas.y = t.extremo2.y
        elif t.extremo2.comparate(casillax, casillay):
            coordenadas.x=t.extremo1.x
            coordenadas.y = t.extremo1.y
    return coordenadas
