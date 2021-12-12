from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

class ListaClienteView(ListView):
    model = Cliente
    queryset = Cliente.objects.all().order_by('nome_completo')

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    success_url = '/clientes/'

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    success_url = '/clientes/'

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = '/clientes/'




