from figuras import FiguraGeometrica
#se importa la clase desde el archivo

import math
#se importa esta libreria para poder usar pi
class Circulo(FiguraGeometrica):
    #se manda a llamar el atributo de la clase padre
    #agregamos el atributo radio, para determinar el area del circulo
    def __init__(self, nombre,radio=float(input('¿Cuál es el radio?: '))):
        super().__init__(nombre)
        self.radio=radio

    def calcularArea(self):
        #escribimos la formula del circulo
        area=math.pi*(self.radio**2)
        return super().calcularArea(round(area, 2))
#return super().calcularArea(round(area, 2)) para redondear a dos decimales

        
#definimos el nombre d ela figura
nombre='circulo'
circulo=Circulo(nombre)
circulo.calcularArea()