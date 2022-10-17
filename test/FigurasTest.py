import unittest

from src.model.Circulo import Circulo
from src.model.Cuadrado import Cuadrado
from src.model.Programa import Programa



class FigurasTest(unittest.TestCase):

    def test_averiguar_area_cuadrado(self):
        cuadrado = Cuadrado(10)
        area = cuadrado.averiguar_area()
        self.assertEqual(100, area)  # add assertion here

    def test_averiguar_area_cuadrado_valor_incorrecto(self):
        cuadrado = Cuadrado(10)
        area = cuadrado.averiguar_area()
        # La prueba pasa pq si el area se calcula bien el resultado NO será 10
        self.assertFalse(area == 10)  # add assertion here

    def test_averiguar_area_circulo(self):
        circulo = Circulo(2)
        area = circulo.averiguar_area()
        self.assertEqual(12.5664, area)  # add assertion here

    def test_contar_figuras(self):
        ## El constructor actual inicia dos cuadrados y un circulo
        programa = Programa()

        # Verificar que existan un cuadrado y un circulo
        cantCirculos, cantCuadrados = programa.contar_figuras_tipo()
        self.assertTrue(cantCirculos == 1)
        self.assertTrue(cantCuadrados == 2)


if __name__ == '__main__':
    unittest.main()
