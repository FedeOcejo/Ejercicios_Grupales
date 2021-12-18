import os

os.environ["OUTPUT_PATH"] = ""


def CalificacionesEstudiantes(notas):
    lista1 = []
    for i in notas:
        lista1.append(notafinal(i))
    return lista1

def CalificacionFinal(notas):
    notaentera = 0
    if notas < 40:
        notaentera = notas
    else:
        quebrados= int(notas / 5 + 1)
        factor= int(cocientes * 5)
        if factor - notas < 3:
            notaentera = factor
        else:
            notarentera= notas
    return notaentera