from figuras import FiguraGeometrica
import math
import os
os.system('cls')

# Modificamos la clase FiguraGeometrica para el polimorfismo
class FiguraGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre

    def calcularArea(self):
        # Método que será sobrescrito por las subclases
        pass
    
    def mostrar_info(self):
        # Método polimórfico que muestra información de cualquier figura
        area = self.calcularArea()
        print(f"| {self.nombre:12} |  {area:10.2f} |")


#clases de figuras geométricas 
class Circulo(FiguraGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def calcularArea(self):
        area = math.pi * (self.radio ** 2)
        return area  # Retornamos el área en lugar de imprimir

class Rectangulo(FiguraGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = self.base * self.altura
        return area  # Retornamos el área

class Triangulo(FiguraGeometrica):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcularArea(self):
        area = (self.base * self.altura) / 2
        return area  # Retornamos el área



# ===== DEMOSTRACIÓN DE POLIMORFISMO =====
print(".... FIGURAS GEOMÉTRICAS ....")
print("-" * 30)
print(f"| {'Figura':12} | {'Área':12}|")
print("-" * 30)

# Crear un arreglo (lista) de objetos de diferentes figuras
figuras = [
    Circulo("Círculo", 5.0),
    Rectangulo("Rectángulo", 8.0, 6.0),
    Triangulo("Triángulo", 10.0, 7.0),
    Circulo("Círculo", 3.5),
    Rectangulo("Rectángulo", 12.0, 4.0),
    Triangulo("Triángulo", 6.0, 9.0)
]

#recorrer el arreglo con un for 
#aqui esta el polimorfismo
for figura in figuras:
    #el mismo método mostrar_info() se comporta diferente para cada figura
    figura.mostrar_info()

print("-" * 30)




