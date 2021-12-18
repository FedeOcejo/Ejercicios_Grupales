# Ejercicios_Grupales


Mi dirección de github de este repositorio es el siguiente: [Github](https://github.com/FedeOcejo/Ejercicios_Grupales.git)
 
Hemos creado un código en el cual suma los valores de una matriz y te devuelve este como un numero entero, este mediante a funciones como la suma.

Hemos creado un código en el cual se compara el resultado de dos alumnos Lucia y Carlos y te dice quien gano o saco mayor calificacion, en el cual empleamos valoreas aleatorios, parametros, opraciones y ciclos

Hemos creado un código en el cual suma los valores de una matriz sin importar su tamaño y te devuelve este como un numero entero, este mediante a funciones como la suma.

Hemos crado una escalera en la cual tu elijes el tamaño y en cada fila que agreges se agrega un hashtag "#" 

Hemos creado el juego de las piedras a base de listas, diccionarios y bucles

Hemos creado un laberinto con una rana en el cual tenia que salir y para crearlo usamos movimientos aleatorios, un tablero, bucles y condicionales

Hemos credao un ejercicio en el cual cda estudiante recibe una nota entre el 0 y 100, si la nota era inferior a 40 era suspensa, la nota se redondea segun las condiciones puestas en las intrucciones. Las notas son las siguientes:
4
5
67
7
4

Hemos creado un código en el cual determinamos el punto de inicio donde se encuentra la casa. Hemos ubicado los arboles en diferentes punto el manano en el punto a y el nranjo en el punto b, cuando un afruta cae de su árbol atteriza a cierta distancia del árbol de donde cayo a lo largo del eje x

los codigos estan divididos por un agran linea crado con guiones

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
print("la suma de los valores vale", result)

------------------------------------------------------------------------------------------
import math
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
    print("Carlos gano")
------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------

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

        return "\n".join([""*(n-i)+"#"*(i+i-2) for i in range(1,n+1)])
  
n=int(input("indica un numero: "))
print(staircase(n))
------------------------------------------------------------------------------------------
import os
def gameOfStrones (n):
    campeon = " "
    if (mejorjugada(n)!=0):
        campeon= "jugador 1 es el ganador"
    else:
        campeon = "jugador 2 es el ganador"
    return campeon
def mejorjugada(n):
    jugada = 0
    residuo = n%7
    if residuo >= 2 and residuo <=3:
        jugada= 2
    elif residuo ==4:
        jugada = 3
    elif residuo>=5 and residuo<=6:
        jugada = 5
    return jugada

def partida (n):
    intentos =0
    campeon = ""
    while campeon != "jugador 1 es el ganador" and campeon!= "jugador 2 es el gandor":
        jugada1 =mejorjugada(n)
        if jugada1 == 0:
            if n > 5:
                jugada1 = 5
            elif n>3:
                jugada1 =3
            else:
                jugada1 =2
        print ("Juega jugafor 1" + str((intentos%2)+1) + "retirando" + str(jugada1) + "piedras")
        n = n -jugada1
        if(n==1 or n==0):
            campeon= ("P"+str(intentos%2)+1 +"es el ganador")
        intentos+=1
        print (campeon)
if __name__ =="__main__":
    t =int(input().strip())
    for t_itr in range (t):
        n=int(input().strip())
        result = gameOfStrones(n)
------------------------------------------------------------------------------------------
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

def exploracion(casillax, casillay, laberinto, n, m, tuneles):
    numero =0
    den = 0
    prob = 0.0
    if casillax>0 and laberinto[casillax-1][casillay]!= "#":
        den += 1
        if laberinto [casillax-1][casillay]=="%":
            numero+=1
    if casillax<n-1 and laberinto[casillax+1][casillay]!= "#":
        den+= 1
        if laberinto[casillax+1][casillay]=="%":
            numero+=1
    if casillay<m-1 and laberinto[casillax][casillay+1]!="#":
        den+=1
        if laberinto[casillax][casillay+1]=="%":
            numero+=1
    if casillay > 0 and laberinto[casillax][casillay-1]!="#":
        den +=1
        if laberinto[casillax][casillay-1]== "%":
            numero +=1
    if den == 0:
        return prob
    prob = numero/den
    if casillax> 0 and laberinto [casillax-1][casillay]   == "$":
        laberintocopia= laberinto 
        coordenadas= BuscaTunel(casillax-1,casillay,tuneles)
        laberintocopia [casillax][casillay]= "#"
    prob+= exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    if casillax<n-1 and laberinto[casillax+1][casillay]== "$":
        laberintocopia = laberinto
        coordenadas = BuscaTunel(casillax+1,casillay,tuneles)
        laberintocopia[casillax][casillay]="#"

    prob+=exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    if casillay<m-1 and laberinto[casillax][casillay+1]=="$":
        laberintocopia=laberinto
        coordenadas=BuscaTunel(casillax,casillay+1,tuneles)
        laberintocopia[casillax][casillay]="#"
    prob +=exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    if casillay >0 and laberinto[casillax][casillay-1]=="$":
        laberintocopia=laberinto
        coordenadas = BuscaTunel(casillax,casillay,tuneles)
        laberintocopia[casillax][casillay]="#"
    prob += exploracion(coordenadas.x,coordenadas.y,laberintocopia,n,m,tuneles)/den
    return prob
if __name__ == "__main__":
    print ("Dimensiones del laberinto y número de tuneles:(filas,columnas)")
    first_multiple_input = input().rstrip().split()
    n= int(first_multiple_input[0])
    m= int(first_multiple_input[1])
    k= int(first_multiple_input[2])
    laberinto=[]
    for n_itr in range (n):
        print ("Fila"+str(n_itr)+"del laberinto:(# muro, porcentaje salida, *bomba, $ vacía, o tunel")
        row= input()
        laberinto.append(list(row))
    tuneles=[]
    for k_itr in range (k):
        print("Coordenadas (i1 j1 i2 j2) del tunel" + str(k_itr))
        second_multiple_input = input().rstrip().split()
        i1 =int( second_multiple_input[0])
        j1 = int(second_multiple_input[1])
        i2 = int(second_multiple_input[2])
        j2 = int(second_multiple_input[3])
        tuneles.append(Tunel(i1,j1,i2,j2))
    print("Coordenadas iniciales de la rana:")
    third_multiple_input= input().rstrip().split()
    pos1= int(third_multiple_input[0])
    pos2=int(third_multiple_input[1])
    prob= exploracion(pos1,pos2,laberinto,n,m,tuneles)
    print(prob)
------------------------------------------------------------------------------------------
import os

os.environ["OUTPUT_PATH"] = ""


def CalificacionesEstudiantes(notas):
    lista1 = []
    for i in notas:
        lista1.append(notas (i))
    return lista1

def CalificacionFinal(notas):
    notaentera = 0
    if notas < 40:
        notaentera = notas
    else:
        quebrados= int(notas / 5 + 1)
        factor= int(quebrados * 5)
        if factor - notas < 3:
            notaentera = factor
        else:
            notarentera= notas
    return notaentera

    if __name__ == "__main__":
        fptr = open(os.environ["OUTPUT_PATH"] + "Estudiantes.txt", "w")
    print("numero de estudiantes:")
    estudiantes = int(input().strip())

    notas = []

    for _ in range(estudiantes):
        print("nota de cada estudiante:")
        notas1 = int(input().strip())
        notas.append(notas1)

    resultado = CalificacionesEstudiantes(notas)

    fptr.write("\n".join(map(str, resultado)))
    fptr.write("\n")

    fptr.close()
------------------------------------------------------------------------------------------
import re


def contador(a, b, c, d, manzanas, naranjas):
    num_manzanas= 0
    num_naranjas= 0
    for manzana1 in manzanas:
        if c + manzana1 >= a and c <= b:
            num_manzanas+= 1
    for naranja1 in naranjas:
        if d + naranja1 >= a and d <= b:
            num_naranjas+= 1

            print("Han entrado ", str(num_manzanas), " manzanas")
        print("Han entrado ", str(num_naranjas), " naranjas")


    primer = (
        input(
        "Introduzca dos numeros que serán la amplitud de la casa: "
    )
    .rstrip()
    .split()
    )
    segundo = (
        input(
        "Introduzca dos números que serán la distancia entre los dos árboles: "
    )
    .rstrip()
    .split()
    )
    tercero = input("Introduzca dos números: ").rstrip().split()

    a = int(primer[0])
    b = int(primer[1])
    c = int(segundo[0])
    d = int(segundo[1])
    e = int(tercero[0])
    f = int(tercero[1])

    print("distancias a las que cada manzana cae desde el punto c)")
    manzanas = list(map(int, input().rstrip().split()))
    print(
    " distancias a las que cada naranja cae desde el punto d")
    naranjas = list(map(int, input().rstrip().split()))

    contador(a, b, c, d, naranjas, manzanas)
