# Ejercicios_Grupales


Mi dirección de github de este repositorio es el siguiente: [Github](https://github.com/FedeOcejo/Ejercicios_Grupales.git)
 
Hemos creado un código en el cual suma los valores de una matriz y te devuelve este como un numero entero, este mediante a funciones como la suma.

```import math
import os
import random
import re
import sys



def simpleArraySum(ar):
   
    sum = 0
    for numero in ar:
      sum= sum + numero
    return sum


n=int (input("intoduzca la dimension de una matriz: "))
print ("introduce los numeros de la martiz: ", end="")
ar = list(map(int, input().rstrip().split()))
print (ar)
result = simpleArraySum(ar)
print("la suma de los valores vale", result)```

Hemos creado un código en el cual se compara el resultado de dos alumnos Lucia y Carlos y te dice quien gano o saco mayor calificacion, en el cual empleamos valoreas aleatorios, parametros, opraciones y ciclos

```import math
import os
import random 
import re
import sys
from random import randint
from typing import ParamSpecArgs

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
        pointsLU +=1
    elif lucia1 < carlos1:
        pointsCA +=1
    else:
        pass

    if lucia2 > carlos2:
        pointsLU +=1
    elif lucia2 < carlos2:
        pointsCA +=1
    else:
        pass

    if lucia3 > carlos3:
        pointsLU+=1
    elif lucia3 < carlos3:
        pointsCA+=1
    else:
        pass

    print("Lucia saco: ")
    print("carlos saco: ")
    return
if lucia1 + lucia2 + lucia3 > carlos1 + carlos2 + carlos3:
    print("Lucia gano")
else:
    print("Carlos gano")```
    
Hemos creado un código en el cual suma los valores de una matriz sin importar su tamaño y te devuelve este como un numero entero, este mediante a funciones como la suma.

```import math
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
print("la suma de los valores vale", result)```

Hemos crado una escalera en la cual tu elijes el tamaño y en cada fila que agreges se agrega un hashtag "#" 

```import math
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

        return "\n".join([""*(n-i)+"#"*(i+i-2) for i in range(1,n+1)])
  
n=int(input("indica un numero: "))
print(staircase(n))```
