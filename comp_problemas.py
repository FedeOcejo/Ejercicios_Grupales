import math
import os
import random 
import re
import sys
from random import randint

lucia1=randint (1,100)

lucia2=randint (1,100)

lucia3=randint (1,100)

carlos1=randint (1,100)

carlos2=randint (1,100)

carlos3=randint (1,100)


print("Lucia en la primera acividad saco: ")
print("\nClarity={}".format(lucia1))
print("\nOriginality={}".format(lucia2))
print("\nDificulty={}".format(lucia3))


print("Carlos en la primera acividad saco: ")
print("\nClarity={}".format(carlos1))
print("\nOriginality={}".format(carlos2))
print("\nDificulty={}".format(carlos3))


def compareTipelts():
    pointsLU=0
    pointsCA=0

    if lucia1 > carlos1:
        pointsCA+=1