import requests
from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse
from . import forms


class SearchPage(generic.FormView):
    """
    Display the book search form. The form allows users to select a search key
    (title, author or subject) and then enter a search query.
    """
    template_name = 'index.html'
    form_class = forms.SearchForm
    success_url = '/results/'

    def form_valid(self, form):
        return super(SearchPage, self).form_valid(form)


class ResultsPage(generic.TemplateView):
    """
    Get the search results from the OpenLibrary API and display them in the
    browser.
    """
    template_name = 'results.html'
    search_api_url = 'https://openlibrary.org/search.json'

    def get_context_data(self, **kwargs):
        """
        Get the search query entered by the user, and use the query to search
        the OpenLibrary API.
        :param kwargs:
        :return: context data containing the search query and its results
        """
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
            r_json = response.json()
            num_found = r_json['numFound']
            books = r_json['docs']

            context['num_found'] = num_found
            context['search_query'] = search_query
            context['books'] = books

        return context
