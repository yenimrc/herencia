from figuras import FiguraGeometrica
#from figurasG.figuras import FiguraGeometrica
#en caso de que el archo este fuera de la carpeta


class Rectangulo(FiguraGeometrica):
#definimos los atributos base y altura
    def __init__(self, nombre, base=float(input('Medida de la base: ')), altura=float(input('Medida de la altura: ')) ):
        super().__init__(nombre)
        self.base=base
        self.altura=altura

    def calcularArea(self):
        #definimos la formula del area del rectangulo
        area=self.base*self.altura
        return super().calcularArea(area)
        

nombre='Rectangulo'
rectangulo=Rectangulo(nombre)
rectangulo.calcularArea()
