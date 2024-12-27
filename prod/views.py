from django.shortcuts import render
from .models import Product, UserModel, Questions
from .forms import ProductForm
from django.views.generic import ListView, DetailView

class ReadCards(ListView):
    model = Product
    template_name = 'cards.html'
    context_object_name = 'cards'

class DetailCard(DetailView):
    model = Product
    template_name = 'card.html'

