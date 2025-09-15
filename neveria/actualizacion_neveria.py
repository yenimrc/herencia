class ErrorPaleta:
    pass #para paletas que no se encuentran en venta o disponibles

# Clase base para todas las paletas
class Paleta:
    def __init__(self,sabor:str,precio:float):
        if precio<0:
            raise ErrorPaleta(f'Error de paleta no encontrada')
        #atributos de la clase base
        self.sabor=sabor
        self.precio=float(precio)
    def informacion(self):
        #muestra la informacion basica de cada paleta
        print(f'Sabor: {self.sabor}, precio: {self.precio:.2f} ')
    

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

def buscarpaleta(sabor_busqueda):
    for paleta in paletas:
        if paleta.sabor==sabor_busqueda:
            return paleta
    raise ErrorPaleta(f'Paleta {sabor_busqueda} no encontrada en inventario')

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
for paleta in paletas:  
    paleta.informacion()

sabor_a_buscar=['Fresa','Uva']

print(' '*4,'Busqueda de paletas')
for sabor in sabor_a_buscar:
    try:
        sabor_encontrada=buscarpaleta(sabor)
        print('Paleta disponible')
    except ErrorPaleta as error:
        print(f'X {error}')
