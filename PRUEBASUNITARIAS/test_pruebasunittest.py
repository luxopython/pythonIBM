import unittest
from pruebasunittest import area  # Asegúrate de que 'area' está correctamente definida
from math import pi

class TestArea(unittest.TestCase):
    def test_area(self):
        print('-----Test valores de resultado conocido-----')
        
        # Prueba para el radio de 1
        self.assertAlmostEqual(area(1), pi)
        
        # Prueba para el radio de 0
        self.assertAlmostEqual(area(0), 0)
        
        # Prueba para el radio de 3
        self.assertAlmostEqual(area(3), pi * (3 ** 2))

    def test_negativos(self):
        print('-----Test de valores negativos-----')
    
#Indicamos el tipo de excepción,la función y el valor esperado.
        self.assertRaises(ValueError,area, -1)