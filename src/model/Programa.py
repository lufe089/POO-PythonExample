from src.model.Circulo import Circulo
from src.model.Cuadrado import Cuadrado

class Programa():
    def __init__(self):
        self.figuras = []  # Los atributos de instancia deben usar la palabra self
        self._inicizalizar_figuras()

    def _inicizalizar_figuras(self):
        # Agrega figuras para pruebas
        self.figuras.append(Circulo(10))
        self.figuras.append(Cuadrado(5))
        self.figuras.append(Cuadrado(20))

    def agregarFigura(self, lado = None):
        """ Agrega figuras de tipo cuadrado, inicializa los parametros con nombre"""
        self.figuras.append(Cuadrado(lado))

    def agregarFigura(self, radio = None):
        self.figuras.append(Cuadrado(radio))

    def calcular_suma_areas(self):
        # TODO
        print("Pendiente")

    def mostrar_area_figura(self):
        for figura in self.figuras:
            print(f"El area de la figura {figura.get_nombre_figura()} es  {figura.averiguar_area()}")

    def mostrar_perimetro_figura(self):
        for figura in self.figuras:
            print(f"El perimetro de la figura {figura.get_nombre_figura()} es  {figura.averiguar_perimetro()}")

    def contar_figuras_tipo(self):
        """Cuenta cuántas figuras hay de cada tipo"""
        cont_circulos = 0
        cont_cuadrados = 0
        for figura in self.figuras:
            if isinstance(figura, Circulo):
                figura = Circulo(figura)  #Hago el casting
                print("El radio es ",figura._radio)
                cont_circulos += 1
            elif isinstance(figura, Cuadrado):
                cont_cuadrados += 1
        #Python permite el retorno de más de un atributo
        return cont_circulos, cont_cuadrados