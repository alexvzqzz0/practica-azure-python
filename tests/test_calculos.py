import unittest

from src.calculos import sumar, media, contar_prioridades


class TestCalculos(unittest.TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(4, 6), 10)

    def test_media(self):
        self.assertEqual(media([1, 2, 3]), 2)

    def test_media_vacia(self):
        with self.assertRaises(ValueError):
            media([])

    def test_contar_prioridades(self):
        datos = [
            {"prioridad": 1},
            {"prioridad": 2},
            {"prioridad": 1},
        ]
        self.assertEqual(
            contar_prioridades(datos),
            {1: 2, 2: 1}
        )


if __name__ == "__main__":
    unittest.main()
