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