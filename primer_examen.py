# 2. Dada una lista con nombres de personajes de la saga de Avengers ordenados por 
# nombre del superhéroes, de los cuales se conoce:
# nombre del superhéroe, nombre del personaje (puede ser vacio), 
#grupo al que (perteneces puede ser vacio), año de aparición, 
#por ejemplo (Star Lord – Peter Quill – Guardianes de la galaxia - 1976).
# Resolver las siguientes tareas:

# a. Determinar si “Capitana Marvel” está en la lista y mostrar su
# nombre de personaje;

# b. Almacenar los superhéroes que pertenezcan al grupo
# “Guardianes de la galaxia” en una cola e indicar cuantos son.

# c. Mostrar de manera descendente los superhéroes que
# pertenecen al grupo “Los cuatro fantásticos” y “Guardianes de
# la galaxia”.

# d. Listar los superhéroes que tengan nombre de personajes cuyo
# año de aparición sea posterior a 1960.

# e. Hemos detectado que la superhéroe “Black Widow” está mal
#cargada por un error de tipeo, figura como “Vlanck Widow”,
#modifique dicho superhéroe para solucionar este problema.

# f. Dada una lista auxiliar con los siguientes personajes (‘Black
#Cat’, ‘Hulk’, ‘Rocket Racoonn’, ‘Loki’, complete el resto de la
#información), agregarlos a la lista principal en el caso de no
#estar cargados.

# g. Mostrar todos los personajes que comienzan con C, P o S.

# h. Cargue al menos 20 superheroes a la lista.

from lista import Lista
from colas import Cola
from stack import Stack

lista = Lista()
lista_aux = Lista()
cola = Cola()
pila = Stack()

class Superheroe():
    def __init__(self, nombre, personaje, grupo, anio):
        self.nombre = nombre
        self.personaje = personaje
        self.grupo = grupo
        self.anio = anio
    
    def __str__(self):
        return f'{self.nombre} - {self.personaje} - {self.grupo} - {self.anio}'
    
h1 = Superheroe("Hulk", "Bruce Banner", "Guardianes de la galaxia", 2003)
h2 = Superheroe("Rocket Racoonn", "Juan", "Imperio", 2001)
h3 = Superheroe("Loki", "Loki Laufeyson", "Guardianes de la galaxia",  2000)
h4 = Superheroe("Black Cat", "Cameron", "Guardianes de la galaxia",  2005)

heroes = [h1, h2, h3, h4]

s1 = Superheroe("Iron Man", "Tony Stark", "Imperio", 1949)
s2 = Superheroe("Capitán América", "Steve Rogers", "Los Cuatro Fantásticos", 2011)
s3 = Superheroe("Vlanck Widow", "Natasha Romanoff", "Los Cuatro Fantásticos", 2008)
s4 = Superheroe("Thor", "Thor Odinson", "Guardianes de la galaxia", 1999)
s5 = Superheroe("Spider-Man", "Peter Parker", "Guardianes de la galaxia", 1948)
s6 = Superheroe("Capitana Marvel", "Carol Danvers", "Los Cuatro Fantásticos", 2007)
s7 = Superheroe("Black Panther", "T'Challa","Guardianes", 2011)
s8 = Superheroe("Ant-Man", "Scott Lang", "Guardianes de la galaxia", 2008)
s9 = Superheroe("Bruja Escarlata", "Wanda Maximoff", "Los Cuatro Fantásticos", 1902)
s10 = Superheroe("D", "Stephen St","Galaxia",  1999)
s11 = Superheroe("Do", "Stephen S","Galaxia",  1997)
s12 = Superheroe("Doc", "Stephen trange","Galaxia", 1950)
s13 = Superheroe("Doct", "Stephen Stnge","Galaxia",  1992)
s14 = Superheroe("Docto", "Stephen nge","Galaxia",  1993)
s15 = Superheroe("Doctor", "Stephen Stss","Galaxia",  1999)
s16 = Superheroe("Doctor S.", "Stephen aaae","Galaxia",  1915)


super = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]

def cargar():
    for j in super:
        lista.insert(j, 'nombre')

def cargar_h():
    for i in heroes:
        lista.insert(i, 'nombre')

def parte_f():
    cargar_h()
    lista.order_by("nombre", False)

def capitana_marvel():
    encontrada = False
    i = 0
    for i in range(0, lista.size()):
        if lista.get_element_by_index(i).nombre == "Capitana Marvel":
            v = lista.get_element_by_index(i)
            print(v.nombre, ' es: ', v.personaje)
            encontrada = True
    return encontrada

def guardianes():
    for i in range(0, lista.size()):
        if lista.get_element_by_index(i).grupo == "Guardianes de la galaxia":
            v = lista.get_element_by_index(i).nombre
            cola.arrive(v)

def parte_g():
    for i in range(0, lista.size()):
            v = lista.get_element_by_index(i).nombre
            if v[0] == "C" or v[0] == "P" or v[0] == "S":
                print(v)

def selectos():
    for i in range(0, lista.size()):
        if lista.get_element_by_index(i).grupo == "Guardianes de la galaxia" or lista.get_element_by_index(i).grupo == "Los Cuatro Fantásticos":
            v = lista.get_element_by_index(i).nombre
            pila.push(v)

def parte_a():
    if capitana_marvel():
        pass
    else:
        print('Capitana Marvel no se encuentra en la lista.')

def parte_b():
    guardianes()
    print("Hay un total de: ", cola.size(), " superhéroes que pertenecen a Guardianes de la Galaxia.")


def parte_c():
    selectos()
    while pila.size() > 0:
        print(pila.pop())

def parte_d():
    i = 0
    for i in range(0, lista.size()):
        if lista.get_element_by_index(i).anio > 1960:
            v = lista.get_element_by_index(i)
            print(v.personaje, "conocido como: ", v.nombre, "hizo su primera aparición en: ", v.anio)

def corregir():
    for i in range(0, lista.size()):
        if lista.get_element_by_index(i).nombre == "Vlanck Widow":
            v = lista.get_element_by_index(i)
            v.nombre = "Black Widow"

def parte_e():
    corregir()
    lista.order_by("nombre", False)

cargar()
#lista.barrido()
# parte_a()
# parte_b()
# parte_c()
# parte_d()
# parte_e()
parte_f()
lista.barrido()
# parte_g()
