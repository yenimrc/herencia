
class Personaje:
    def __init__(self,nombre,nivel):
         #atributos comunes a todos los personajes
        self.nombre=nombre
        self.nivel=nivel

    def atacar(self):
        #metodo comun de los personajes "atacar"
        print('Atacando...')

    def mostrar_info(self):  
        #muestra la informacion completa del jugador
        print(f'Jugador: {self.nombre}, Nivel: {self.nivel}')


class Jugador(Personaje):
    def __init__(self, nombre, nivel,clase):
        super().__init__(nombre, nivel)
        #atributo adicional específico de jugadores
        self.clase=clase

    def atacar(self):
        if self.clase == "Guerrero":
            print(f"⚔️ {self.nombre} (Guerrero) ataca con espada - Daño: {self.nivel * 3}")
        elif self.clase == "Mago":
            print(f"🧙 {self.nombre} (Mago) lanza hechizo - Daño: {self.nivel * 8}")
        elif self.clase == "Arquero":
            print(f"🏹 {self.nombre} (Arquero) dispara flecha - Daño: {self.nivel * 9}")  
        else:
            print(f"{self.nombre} ataca de manera genérica")

    def mostrar_info(self):
        #POLIMORFISMO: Mismo método, información diferente
        print(f"JUGADOR: {self.nombre} | Nivel: {self.nivel} | Clase: {self.clase}")        

    def habilidadespecial(self):
        print(f'Tiene la habilidad de: {self.clase}')


class Enemigo(Personaje):
    def __init__(self, nombre, nivel,tipo):
        super().__init__(nombre, nivel)
        #atributo adicional específico de Enemigo
        self.tipo=tipo
    def atacar(self):
        # POLIMORFISMO: Mismo método, comportamiento diferente
        if self.tipo == "Esqueleto":
            print(f"💀 {self.nombre} (Esqueleto) ataca con hueso - Daño: {self.nivel * 5}")
        elif self.tipo == "Ogro":
            print(f"👹 {self.nombre} (gro) ataca con garrote - Daño: {self.nivel * 7}")
        elif self.tipo == "Dragón":
            print(f"🐉 {self.nombre} (Dragón) lanza fuego - Daño: {self.nivel * 15}")
        else:
            print(f"{self.nombre} ataca de manera genérica")
    
    def mostrar_info(self):
        # POLIMORFISMO: Mismo método, información diferente
        print(f"ENEMIGO: {self.nombre} | Nivel: {self.nivel} | Tipo: {self.tipo}")

    def gritar(self):
        print('HUUUUUUURRRRGGGHH')
 

personajes = [
    Jugador('Merlin', 8, 'Mago'),      
    Jugador('Eliot', 6, 'Caballero'),  
    Enemigo('Grow', 12, 'Ogro'),      
    Enemigo('Thesan', 5, 'Dragón')   
]


for personaje in personajes:
    personaje.mostrar_info()  
    personaje.atacar()
