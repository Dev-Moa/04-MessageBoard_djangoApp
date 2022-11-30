from django.shortcuts import render
from django.views.generic import ListView
from .models import posts
# Create your views here.
class HomePageView(ListView):
    model = posts
    template_name = 'index.html'