from django.shortcuts import render
from django.views.generic import TemplateView

class AppHomeView(TemplateView):
    template_name = 'home.html'
