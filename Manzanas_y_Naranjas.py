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
