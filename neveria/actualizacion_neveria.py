from abc import ABC, abstractmethod

# Clase base para todas las paletas
class Paleta(ABC):
    def __init__(self,sabor:str,precio:float):
        #atributos de la clase base
        self.sabor=sabor
        self.precio=float(precio)

    @abstractmethod
    def informacion(self):
        #metodo que sera implentado por las subclases
        pass

    @abstractmethod
    def descuento(self):
        #metodo que sera implentado por lasubclases
        pass
    

class PaletaAgua(Paleta):
    def __init__(self, sabor, precio,base_agua):
        #llama al constructor de la clase base (Paleta)
        super().__init__(sabor, precio)
        #atributo adicional específico de paletas de agua
        self.base_agua=base_agua

    def informacion(self):
        #sobrescribe el método de la clase base
        tipo = "con base de agua" if self.base_agua else "sin base de agua"
        print(f"Paleta de Agua - Sabor: {self.sabor}, Precio: ${self.precio:.2f} ({tipo})")
    
    def descuento(self,porcentaje):
        #para calcular el descuento
        return self.precio *(1-porcentaje/100)

#clase derivada para paletas de crema
class PaletaCrema(Paleta):
    def __init__(self, sabor, precio,crema):
        super().__init__(sabor, precio)
        #atributo adicional específico de paletas de crema
        self.crema=crema

    def informacion(self):
        #sobrescribe el método de la clase base 
        textura = "cremosa" if self.crema else "no cremosa"
        print(f"Paleta de Crema - Sabor: {self.sabor}, Precio: ${self.precio:.2f} ({textura})")   

    def descuento(self,porcentaje):
        #descuento pra paletas a base de crema
        descuento_extra=0.05 if self.crema else 0
        return self.precio * (1-porcentaje/100 + descuento_extra)

#creamos la lista de paletas
paletas = [
    PaletaAgua("Fresa", 10.0, True),
    PaletaAgua("Limon", 8.0, False),
    PaletaCrema("Chocolate", 12.0, True),
    PaletaCrema("Vainilla", 10.0, False),
    PaletaAgua("Mango", 9.0, True),
    PaletaCrema("Café", 15.0, True)
]

print(' '*3,'Paletas disponibles')
print(f"{'Tipo':<15} {'Sabor':<10} {'Precio':<8} {'Descuento 5%':<12} {'Base':<10}")

for paleta in paletas:  
    #tipo de paleta
    tipo='Agua' if isinstance(paleta, PaletaAgua) else 'A base de crema'
    if isinstance(paleta,PaletaAgua):
        informacion='Agua'
    else:
        informacion='Con crema' 
    #para calcular descuento
    descuento=paleta.descuento(5)
    print(f"{tipo:<15} {paleta.sabor:<10} ${paleta.precio:<7.2f} ${descuento:<11.2f} {informacion:<10}")
   


