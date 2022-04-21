import unittest

from src.model.Circulo import Circulo
from src.model.Cuadrado import Cuadrado
from src.view.GUIConsola import GUIConsola


class FigurasTest(unittest.TestCase):

    def test_averiguar_perimetro_cuadrado(self):
        cuadrado = Cuadrado(10)
        area = cuadrado.averiguar_area()
        self.assertEqual(area, 100)  # add assertion here

    def test_averiguar_perimetro_circulo(self):
        circulo = Circulo(2)
        area = circulo.averiguar_area()
        self.assertEqual(area, 12.5664)  # add assertion here

    def test_contar_figuras(self):
        ## El constructor actual inicia dos cuadrados y un circulo
        consola = GUIConsola()

        # Verificar que existan un cuadrado y un circulo
        cantCirculos, cantCuadrados = consola.contar_figuras_tipo()
        self.assertTrue(cantCirculos == 1)
        self.assertTrue(cantCuadrados == 2)


if __name__ == '__main__':
    unittest.main()
