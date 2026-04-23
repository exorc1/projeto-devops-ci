# test_app.py
import unittest
from app import somar, subtrair, multiplicar, dividir, quadrado

class TestApp(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 999)

    def test_subtrair(self):
        self.assertEqual(subtrair(10, 5), 5)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 4), 12)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_quadrado(self):
        self.assertEqual(quadrado(4), 16)

if __name__ == '__main__':
    unittest.main()
