import unittest

from recursao.fatorial import factorial


class FactorialTest(unittest.TestCase):

    def test_fatorial_encadeado_quando_valor_eh_igual_zero(self):
        resultado = factorial(0)
        self.assertEqual(1, resultado)

    def test_fatorial_encadeado_quando_valor_eh_negativo(self):
        with self.assertRaises(ValueError) as context:
            factorial(-1)

        self.assertEqual(context.exception.__class__.__name__, 'ValueError')

    def test_fatorial_encadeado_quando_valor_eh_positivo_maior_que_zero(self):
        resultado = factorial(3)
        self.assertEqual(6, resultado)
