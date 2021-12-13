from django.forms import forms
from django.test import TestCase

from ..forms import ClienteForm

class ClienteFormTestCase(TestCase):
    
   # def test_cliente_form_valido(self):
     #   form = ClienteForm(data={
      #      'nome_completo' : "Leonardo Fernandes",
       #     'data_nascimento' : "01-01-1998",
        #    'ativo' : "Sim"
    #})
    #self.assertTrue(forms.is_valid())

    def test_cliente_form_valido(self):
        form = ClienteForm(data={})
        self.assertFalse(form.is_valid())