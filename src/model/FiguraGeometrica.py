from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    def __init__(self):
        # Atributos  de instancia protegidos
        self._perimetro = 0
        self._area = 0
        self._nombre_figura = " "

    @abstractmethod
    def averiguar_perimetro(self):
        pass

    @abstractmethod
    def averiguar_area(self):
        pass

    def get_perimetro(self):
        if self.perimetro == 0:
            # Si no ha calculado se calcula  primero
            self.averiguar_perimetro()
        return self._perimetro

    def get_area(self):
        #TODO: Hacer el mismo ajuste de perimetro para area
        return self._area

    def get_nombre_figura(self):
        return self._nombre_figura
