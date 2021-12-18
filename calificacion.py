import os

os.environ["OUTPUT_PATH"] = ""


def CalificacionesEstudiantes(notas):
    lista1 = []
    for i in notas:
        lista1.append(notafinal(i))
    return lista1