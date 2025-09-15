import os
os.system('cls')

from abc import ABC, abstractmethod

#creamos las clases abstractas, para las habilidades
class HabilidadesMagicas(ABC):
    @abstractmethod 
    def hechizo(self):
        pass

class HabilidadesFisicas(ABC):
    @abstractmethod
    def defensa(self):
        pass
    @abstractmethod
    def ataque_f(self):
        pass


#clase padre
class Personaje(ABC):
    def __init__(self,nombre,nivel):
        self.nombre=nombre
        self.nivel=nivel

    @abstractmethod
    def atacar(self):
        pass
    def caracteristicas_personaje(self):
        try:
            #comprobamos nivel
            if self.nivel==1:
                print('Este personaje tiene un nivel muy bajo')
        except:
            print('Elige otro personaje con un nivel más alto')

class Jugador(Personaje, HabilidadesMagicas):
    def __init__(self, nombre, nivel,personaje):
        super().__init__(nombre, nivel)
        self.personaje=personaje

    def atacar(self):
        print(f'{self.nombre}, esta preparando su ataque')

    def hechizo(self):
        print(f'{self.nombre}, lanzo su echizo mas poderoso')

    def mostrar_info(self):  
        print(f'Jugador: {self.nombre}, Nivel: {self.nivel}, Tipo de personaje: {self.personaje}')


class Enemigo(Personaje, HabilidadesFisicas):
    def __init__(self, nombre, nivel,criatura):
        super().__init__(nombre, nivel)
        self.criatura=criatura

    def atacar(self):
        print(f'{self.nombre}, listo para atacar')
    
    def defensa(self):
        print(f'{self.nombre}, se protege')

    def ataque_f(self):
        print(f'{self.nombre} se cubre de los hechizos')

    def mostrar_info(self):  
        print(f'Enemigo: {self.nombre}, Nivel: {self.nivel}, Tipo de creatura: {self.criatura}')

#este personaje tiene ambas habilidades
class PersonajeEspecial(Personaje, HabilidadesMagicas, HabilidadesFisicas):
    def __init__(self, nombre, nivel,personaje):
        super().__init__(nombre, nivel)
        self.personaje=personaje
    
    def atacar(self):
        print(f'{self.nombre} combina magia y fuerza en su ataque')

    def hechizo(self):
        print(f'{self.nombre}, lanza el hechizo que desprende una luz brillante')

    def defensa(self):
        print(f'{self.nombre}, se protege con un escudo invisible')

    def ataque_f(self):
        print(f'{self.nombre} ataca con su anillo magico')

    def mostrar_info(self):  
        print(f'Personaje especial: {self.nombre}, Nivel: {self.nivel}, Tipo: {self.personaje}')

heroe1=Jugador('Rhys',8,'principe')
heroe2=Jugador('Oz',1,'mago')
j_especial=PersonajeEspecial('Tamlin',10,'campeón invicto')
contrincante1=Enemigo('Grow',12,'ogro')
contrincante2=Enemigo('Thesan',5,'caballero')

print('---JUGADORES---')
heroe1.mostrar_info()
heroe2.mostrar_info()
j_especial.mostrar_info()

print('----Enemigos----')
contrincante1.mostrar_info()
contrincante2.mostrar_info()

print('---En el campo de batalla---')
heroe2.atacar()
contrincante2.defensa()
j_especial.hechizo()

