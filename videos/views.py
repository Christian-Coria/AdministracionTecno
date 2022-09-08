from django.shortcuts import render
from django.views.generic import TemplateView


class Curso(TemplateView):
    template_name = "videos/curso.html"
