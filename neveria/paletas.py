# Clase base para todas las paletas
class Paleta:
    def __init__(self,sabor:str,precio:float):
        #atributos de la clase base
        self.sabor=sabor
        self.precio=float(precio)
    def informacion(self):
        #muestra la informacion basica de cada paleta
        print(f'Sabor: {self.sabor}, precio: {self.precio} ')

class PaletaAgua(Paleta):
    def __init__(self, sabor, precio,base_agua):
        #llama al constructor de la clase base (Paleta)
        super().__init__(sabor, precio)
        #atributo adicional específico de paletas de agua
        self.base_agua=base_agua
    def mostrarBaseAgua(self):
            #muestra si la paleta es a base de agua o no
            tipo_base = "Sí tiene base de agua" if self.base_agua else "No tiene base de agua"
            print(tipo_base)

#clase derivada para paletas de crema
class PaletaCrema(Paleta):
    def __init__(self, sabor, precio,crema):
        super().__init__(sabor, precio)
        #atributo adicional específico de paletas de crema
        self.crema=crema

    def mostrar_textura_cremosa(self):
        #muestra si la paleta es a base de crema o no
        textura = "Sí tiene textura cremosa" if self.crema else "No tiene textura cremosa"
        print(textura)    


print("\n--- Paletas de Agua ---")
paleta_agua1 = PaletaAgua("Fresa", 10.0, True)
paleta_agua2 = PaletaAgua("Mango", 15.0, True)
paleta_agua1.informacion()
paleta_agua2.informacion()
print(' ')
print("\n--- Paleta de Crema ---")
paleta_crema1 = PaletaCrema("Chocolate", 25.0, True)
paleta_crema2 = PaletaCrema("Galleta", 29.0, True)
paleta_crema1.informacion()
paleta_crema2.informacion()



