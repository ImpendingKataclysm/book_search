import requests
from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse
from . import forms


class SearchPage(generic.FormView):
    template_name = 'index.html'
    form_class = forms.TitleSearchForm
    success_url = '/results/'

    def form_valid(self, form):
        search_query = form.cleaned_data['book_title']
        return super(SearchPage, self).form_valid(form)


class ResultsPage(generic.TemplateView):
    template_name = 'results.html'
    search_api_url = 'https://openlibrary.org/search.json'

    def get_context_data(self, **kwargs):
        context = super(ResultsPage, self).get_context_data()
        search_query = self.request.GET.get('book_title')

        if search_query:
            response = requests.get(self.search_api_url, params={'title': search_query})
            books = response.json()['docs']
            titles = [book['title'] for book in books]
            context['search_query'] = search_query
            context['books'] = books

        return context
