import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        palabra='buenos dias'
        resultado=cambia_texto.todo_mayuscula(palabra)
        self.assertEqual(resultado,'BUENOS DIAS')

if __name__=='__main__':
    unittest.main()
