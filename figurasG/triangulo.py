from figuras import FiguraGeometrica


class Triangulo(FiguraGeometrica):
    #mandamos a traer los atributos de la clase padre
    #definimos los atributos base y altura
    def __init__(self, nombre, base=float(input('Medida de la base: ')), altura=float(input('Medida de la altura: ')) ):
        super().__init__(nombre)
        self.base=base
        self.altura=altura

    def calcularArea(self):
        #definimos la formula del area del triangulo
        area=self.base*self.altura / 2
        return super().calcularArea(area)

nombre='triangulo'
rectangulo=Triangulo(nombre)
rectangulo.calcularArea()

