from django import forms
from django.forms import fields, models
from .models import Cliente


class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}
        )
    )
    class Meta:
        model = Cliente
        fields = ['nome_completo', 'data_nascimento', 'ativo']
