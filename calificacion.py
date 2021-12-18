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