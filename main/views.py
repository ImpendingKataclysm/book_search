from django.shortcuts import render
from django.views import generic
from . import forms


class SearchPage(generic.FormView):
    template_name = 'index.html'
    form_class = forms.TitleSearchForm
    success_url = '/'
