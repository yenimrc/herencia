class FiguraGeometrica:
    #definimos el atributo d ela clase padre
    def __init__(self,nombre):
        self.nombre=nombre

    def calcularArea(self,area):
        #definimos el mensaje que se mostrara, para que se de a conocer el nombre y area de la figura
        print(f'El área de la figura {self.nombre} es de: {area}')


