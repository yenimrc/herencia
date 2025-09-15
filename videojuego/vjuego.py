import os
os.system('cls')

class NiveldeError(Exception):
        pass

class Personaje:
    def __init__(self,nombre,nivel):
        #verificamos si el nivel es menor o igual a 1
        if nivel<1:
            raise NiveldeError('Elije otro personaje con un mayor nivel')
        self.nombre=nombre
        self.nivel=nivel

    def atacar(self):
        #verificamos si el nicel es menor a 5
        if self.nivel<5:
            raise NiveldeError('Este personaje tiene un nivel muy bajo. Mayor posibilidad de perder.')
        print('Atacando...')


class Jugador(Personaje):
    def __init__(self, nombre, nivel,personaje):
        super().__init__(nombre, nivel)
        self.personaje=personaje

    def habilidadespecial(self):
        print('Inmovilizar')

    def mostrar_info(self):  
        print(f'Jugador: {self.nombre}, Nivel: {self.nivel}, Tipo de personaje: {self.personaje}')


class Enemigo(Personaje):
    def __init__(self, nombre, nivel,criatura):
        super().__init__(nombre, nivel)
        self.criatura=criatura

    def gritar(self):
        print('HUUUUUUURRRRGGGHH')

    def mostrar_info(self):  
        print(f'Enemigo: {self.nombre}, Nivel: {self.nivel}, Tipo de creatura: {self.criatura}')

heroe1=Jugador('Rhys',8,'principe')
heroe2=Jugador('Oz',1,'mago')
contrincante1=Enemigo('Grow',12,'ogro')
contrincante2=Enemigo('Thesan',5,'caballero')

print('---JUGADORES---')
try:
    heroe1.mostrar_info()
except NiveldeError as error:
    print(f'Error: {error}')

try:
    heroe2.mostrar_info()
except NiveldeError as error:
    print(f'Error: {error}')

print(' ')
print('---Enemigos---')
try:
    contrincante1.mostrar_info()
except NiveldeError as error:
    print(f'Error: {error}')

try:
    contrincante2.mostrar_info()
except NiveldeError as error:
    print(f'Error: {error}')

print(' ')
print('---Acciones---')
try:
    heroe2.atacar()
except NiveldeError as error:
    print(f'Parece que alguien va perdiendo la batalla {heroe2.nombre}: {error}')

try:
    contrincante1.gritar()
    heroe1.habilidadespecial()
except NiveldeError as error:
    print(f'Error: {error}')
