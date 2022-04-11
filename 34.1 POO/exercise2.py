class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return self.lado * 4


quadrado = Quadrado(5)

print(quadrado.calcular_area())
print(quadrado.calcular_perimetro())
