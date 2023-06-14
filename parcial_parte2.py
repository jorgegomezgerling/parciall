#3. Se recuperó la bitácora de la nave del cazarrecompensas Boba Fett, la
#cual se almacenaban en una pila en cada misión de caza que
#emprendió (con la siguiente información planeta visitado, a quien
#capturado, costo de la recompensa), resolver las siguientes
#actividades:
#a. Mostrar los planetas visitados en el orden hizo las misiones.
#b. Determinar cuántos créditos galácticos recaudo en total.
#c. Determinar el número de la misión en que capturo a Han Solo
#y en que planeta fue, suponga que dicha misión está cargada.

from stack import Stack

pila = Stack()
pila_aux = Stack()

class Bitacora:
    def __init__(self, planeta, capturado, recompensa):
        self.planeta = planeta
        self.capturado = capturado
        self.recompensa = recompensa
    
    def __str__(self):
        return f'{self.planeta} - {self.capturado} - {self.recompensa}'
    
b1 = Bitacora("numir", "juan", 1)
b2 = Bitacora("lumir", "alberto", 2)
b3 = Bitacora("tumir", "charly", 3)
b4= Bitacora("gumir", "Han Solo", 4)
b5 = Bitacora("pumir", "fito", 5)


recuerdos = [b1, b2, b3, b4, b5]

for i in recuerdos:
    pila.push(i)

def intercambio():
    while pila.size() > 0:
        pila_aux.push(pila.pop())

def parte_a():
    intercambio()
    print("El orden en el que fueron visitados es: ")
    while pila_aux.size() > 0:
        print(pila_aux.pop())

def parte_b():
    c = 0
    while pila.size() > 0:
        v = pila.pop()
        c = c + v.recompensa
    print(c)

def parte_c():
    pos = 1
    intercambio()
    while pila_aux.size() > 0:
        v = pila_aux.pop()
        if v.capturado == "Han Solo":
            print("Han Solo fue capturado en la misión: ", pos, "en el planeta: ", v.planeta)
        else:
            pos = pos + 1



# parte_a()
# parte_b()
parte_c()
