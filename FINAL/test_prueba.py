import unittest
from unittest import mock

from unittest.mock import patch  # Importar correctamente 'patch' desde mock
from prueba import Inventario, Producto  # Asegúrate de que los nombres sean correctos

class TestGestionDeStock(unittest.TestCase):

    def setUp(self):
        # Crear un inventario vacío para cada prueba
        self.inventario = Inventario()

    @patch('builtins.input', side_effect=["Manzana", "Frutas", "10", "5"])  # Simulando entradas para agregar producto
    def test_agregar_producto(self, mock_input):
        self.inventario.agregar_producto("Manzana")
        self.assertEqual(len(self.inventario.inventario), 1)
        producto = self.inventario.inventario[0]
        self.assertEqual(producto.get_nombre(), "Manzana")
        self.assertEqual(producto.get_categoria(), "Frutas")  # Corregir: debe ser "Frutas"
        self.assertEqual(producto.get_precio(), 10)
        self.assertEqual(producto.get_cantidad(), 5)

    @patch('builtins.input', side_effect=["20"])  # Simulando precio para modificar
    def test_modificar_precio(self, mock_input):
        # Agregar producto inicial
        self.inventario.agregar_producto("Manzana")
        # Modificar el precio
        self.inventario.modificar_precio("Manzana")
        # Verificar si el precio fue modificado
        producto = self.inventario.inventario[0]
        self.assertEqual(producto.get_precio(), 20)

    def test_eliminar_producto(self):
        self.inventario.agregar_producto("Manzana")
        self.assertEqual(len(self.inventario.inventario), 1)
        self.inventario.eliminar_producto("Manzana")
        self.assertEqual(len(self.inventario.inventario), 0)

    def test_buscar_producto(self):
        self.inventario.agregar_producto("Manzana")
        self.assertTrue(self.inventario.buscar_producto("Manzana"))
        self.assertFalse(self.inventario.buscar_producto("Pera"))

    def test_listar_inventario(self):
        self.inventario.agregar_producto("Manzana")
        self.inventario.agregar_producto("Pera")
        with patch('builtins.print') as mock_print:
            self.inventario.listar_inventario()
            mock_print.assert_any_call("Nombre: Manzana")
            mock_print.assert_any_call("Nombre: Pera")


if __name__ == "__main__":
    unittest.main()
