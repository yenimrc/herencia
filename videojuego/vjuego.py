import os
os.system('cls')
class Personaje:
    def __init__(self,nombre,nivel):
        self.nombre=nombre
        self.nivel=nivel

    def atacar(self):
        print('Atacando...')

class Jugador(Personaje):
    def __init__(self, nombre, nivel,mago):
        super().__init__(nombre, nivel)
        self.mago=mago

    def habilidadespecial(self):
        print('Inmovilizar')

    def mostrar_info(self):  
        print(f'Jugador: {self.nombre}, Nivel: {self.nivel}, Tipo de mago: {self.mago}')


class Enemigo(Personaje):
    def __init__(self, nombre, nivel,dragon):
        super().__init__(nombre, nivel)
        self.dragon=dragon

    def gritar(self):
        print('HUUUUUUURRRRGGGHH')

    def mostrar_info(self):  
        print(f'Jugador: {self.nombre}, Nivel: {self.nivel}')

heroe1=Jugador('Merlin',8,'clásico')
heroe2=Jugador('Oz',6,'inventor')
contrincante1=Enemigo('Grow',12,'i')
contrincante2=Enemigo('Thesan',5,'o')

print('---JUGADORES---')
heroe1.mostrar_info()
heroe2.mostrar_info()
print(' ')

print('---Enemigos---')
contrincante1.mostrar_info()
contrincante2.mostrar_info()
print(' ')

print('---Acciones---')
heroe1.atacar()
contrincante2.gritar()
heroe1.habilidadespecial()
