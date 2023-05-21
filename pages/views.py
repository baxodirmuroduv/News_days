from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePagesView(TemplateView):
    template_name = 'home.html'
