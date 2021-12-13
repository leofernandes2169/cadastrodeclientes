from django.test import TestCase
from ..models import Cliente
# Create your tests here.

class ClienteTesrCase(TestCase):

    def setUp(self):
        Cliente.objects.create(
            nome_completo="Leonardo",
            data_nascimento="1998-1-1",
            ativo="True"
        )
    def test_retorno_str(self):
        
        p1 = Cliente.objects.get(nome_completo='Leonardo')
        self.assertEquals(p1.__str__(), 'Leonardo')
        
        

