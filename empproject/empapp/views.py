from django.shortcuts import render
from django.views.generic import ListView, DetailView,UpdateView,CreateView,DeleteView
from .models import Emp
from django.urls import reverse_lazy

# Create your views here.
class emplistview(ListView):
    model=Emp

class empcreateview(CreateView):
    model=Emp
    fields='__all__'

class empupdateview(UpdateView):
    model=Emp
    fields=('age',)

class empdeleteview(DeleteView):
    model=Emp
    success_url = reverse_lazy('list')