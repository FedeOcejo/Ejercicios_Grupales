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