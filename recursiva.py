# 1. Desarrollar una función recursiva que permita contar cuantas veces
#aparece una determinada palabra, en un vector de palabras.

def palabras_r(p, v):
    if len(v) == 0:
        return 0
    else:
        return (1 if v[0] == p else 0) + palabras_r(p, v[1:])

vector = ["juan", "san", "martin", "juan"]

print(palabras_r("san", vector))
