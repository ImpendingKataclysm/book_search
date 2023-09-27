from django.shortcuts import render
from django.views import generic


class SearchPage(generic.TemplateView):
    template_name = 'index.html'
