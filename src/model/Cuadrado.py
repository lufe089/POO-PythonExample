from src.model.FiguraGeometrica import FiguraGeometrica


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        # Invocacion constructor clase padre
        FiguraGeometrica.__init__(self)

        self._lado = lado
        self._nombre_figura = "Cuadrado"

    def averiguar_perimetro(self):
        # Si no se ha calculado previamente se calcula
        if self._perimetro  == 0:
            self._perimetro = self._lado * 4  # Se actualiza el atributo protegido de la clase
        return self._perimetro

    def averiguar_area(self):
        if self._area == 0:
            self._area = pow(self._lado, 2)
        return self._area
