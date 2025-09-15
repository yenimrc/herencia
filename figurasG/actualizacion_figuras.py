from figuras import FiguraGeometrica
import math
import os
os.system('cls')

class ErrorFigura(Exception):
    pass #podemos personalizar el tipo de error

#modificamos la clase FiguraGeometrica para el polimorfismo
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcularArea(self):
        #metodo que será sobrescrito por las subclases
        pass

    def perimetro(self):
        #metodo que sera escrito por las subclases
        pass
    
    def mostrar_info(self):
        #metodo polimórfico que muestra información de cualquier figura
        try:
            area = self.calcularArea()
            perimetro= self.perimetro()
            print(f"| {self.nombre:12} |  {area:10.2f} | {perimetro:10.2f} |")
        except ZeroDivisionError:
            print(f"| {self.nombre:12} |  {'ERROR':10} | {'ERROR':10} |")
    

#clases de figuras geométricas 
class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        if radio<=0:
            raise ErrorFigura('INSERTA OTRO NÚMERO QUE NO SEA 0')
        self.radio = radio

    def calcularArea(self):
        area = math.pi * (self.radio ** 2)
        return area  #retornamos el área en lugar de imprimir
    
    def perimetro(self):
        super().perimetro()
        perimetro=2*math.pi*self.radio
        return perimetro

class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        if base<=0 or altura<=0:
            raise ErrorFigura('INSERTA OTRO NÚMERO QUE NO SEA 0')
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = self.base * self.altura
        return area  #retornamos el área
    
    def perimetro(self):
        super().perimetro()
        perimetro=2*(self.altura+self.base)
        return perimetro

class Triangulo(FiguraGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = (self.base * self.altura) / 2
        return area  #retornamos el área
    
    def perimetro(self):
        super().perimetro()
        #asumiendo que es un triangulo rectangulo
        hipotenusa=math.sqrt(self.base**2 + self.altura**2)
        perimetro=self.base + self.altura + hipotenusa
        return perimetro



# ===== DEMOSTRACIÓN DE POLIMORFISMO =====
print(" "*3,"....... FIGURAS GEOMÉTRICAS .......")
print("-" * 45)
print(f"| {'Figura':12} | {'Área':12} | {'Perimetro':10} |")
print("-" * 45)

#creamos un arreglo (lista) de objetos de diferentes figuras
figuras = [
    Circulo("Círculo", 0), #insertamos un circulo de r=0 para mostrar el mensaje
    #si se cambia el radio por otro numero >0 se deberia de ejecutar sin problema
    Rectangulo("Rectángulo", 8.0, 6.0),
    Triangulo("Triángulo", 0, 7.0),
    Circulo("Círculo", 3.5),
    Rectangulo("Rectángulo", 12.0, 4.0),
    Triangulo("Triángulo", 6.0, 9.0)
]

#recorrer el arreglo con un for 
#aqui esta el polimorfismo
for figura in figuras:
    #el mismo método mostrar_info() se comporta diferente para cada figura
    figura.mostrar_info()

print("-" * 45)




