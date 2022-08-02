from django.test import TestCase
from .models import Vehiculo
# Create your tests here.
class ModelVehiculoTestCase(TestCase):
    
    def setUp(self):
        Vehiculo.objects.create(modelo="modelo de prueba n1", resumen="1231241234", descripcion="eeeeeeeee1111111", categoria="2222222222123456789456123123")
    
    def test_vehiculo_modelo(self):
        prueba_modelo = Vehiculo.objects.get(modelo="modelo de prueba n1")
        # prueba_resumen = Vehiculo.objects.get(resumen="1231241234")
        # prueba_descripcion = Vehiculo.objects.get(descripcion="eeeeeeeee1111111")
        # prueba_categoria = Vehiculo.objects.get(categoria="2222222222123456789456123123")
        self.assertEqual(prueba_modelo, "modelo de prueba n1")
        # self.assertEqual(prueba_resumen, "1231241234")
        # self.assertEqual(prueba_descripcion, "eeeeeeeee1111111")
        # self.assertEqual(prueba_categoria , "2222222222123456789456123123")

