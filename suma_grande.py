import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
  
    sum = 0
    for numero in ar:
        sum= sum + numero
    return sum


n=int (input("intoduzca la dimension de una matriz: "))
print ("introduce los numeros de la martiz: ", end="")
ar = list(map(int, input().rstrip().split()))
print (ar)
result = aVeryBigSum(ar)
print("la suma de los valores vale", result)