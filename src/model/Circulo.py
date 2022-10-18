from src.model.FiguraGeometrica import FiguraGeometrica


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        # Invocacion constructor clase padre
        FiguraGeometrica.__init__(self)

        self._radio = radio
        self._nombre_figura = "Circulo"
        self._PI = 3.1416

    def averiguar_perimetro(self):
        if self._perimetro == 0:
            self._perimetro = 2 * self._PI * self._radio
        return self._perimetro

    def averiguar_area(self):
        if self._area == 0:
            self._area = (pow(self._radio, 2)) * self._PI
        return  self._area
