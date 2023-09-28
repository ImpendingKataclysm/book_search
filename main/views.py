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
        return super(SearchPage, self).form_valid(form)


class ResultsPage(generic.TemplateView):
    template_name = 'results.html'
    search_api_url = 'https://openlibrary.org/search.json'

    def get_context_data(self, **kwargs):
        context = super(ResultsPage, self).get_context_data()
        search_query = None
        params = None
        title = self.request.GET.get('book_title')
        author = self.request.GET.get('author_name')
        subject = self.request.GET.get('subject_keyword')

        if title:
            search_query = title
            params = {'title': search_query}

        if author:
            search_query = author
            params = {'author': author}

        if subject:
            search_query = subject
            params = {'subject': subject}

        if search_query:
            response = requests.get(self.search_api_url, params=params)
            books = response.json()['docs']
            context['search_query'] = search_query
            context['books'] = books

        return context
