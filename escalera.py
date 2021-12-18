import math
import os
import random
import re
import sys

def staircase(n):

    for i in range(1, n+1):
        num_esp= n -(i)

    for i in range (0, int((num_esp)/2)):
        print(" ",end="")

    for i in range (0, n-num_esp):
        print("#", end="")

        return "\n".join([""*(n-i)+"#"*(i+i-24) for i in range(1,n+1)])
  
n=int(input("indica un numero: "))
print(staircase(n))
