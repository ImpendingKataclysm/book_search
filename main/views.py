from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse
from . import forms


class SearchPage(generic.FormView):
    template_name = 'index.html'
    form_class = forms.TitleSearchForm
    success_url = '/results/'

    def form_valid(self, form):
        return super(SearchPage, self).form_valid()


class ResultsPage(generic.TemplateView):
    template_name = 'results.html'

    def get_context_data(self, **kwargs):
        context = super(ResultsPage, self).get_context_data()
        context['search_query'] = self.request.GET['book_title']

        return context
