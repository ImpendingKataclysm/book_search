import requests
from django.views import generic
from . import forms

API_URL = 'https://openlibrary.org'


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
    search_api_url = f'{API_URL}/search.json'

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


class BookDetailPage(generic.TemplateView):
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailPage, self).get_context_data()
        book_id = kwargs['id']
        query = f'{API_URL}/works/{book_id}.json'
        response = requests.get(query)
        r_json = response.json()

        context['query_params'] = self.request.GET.items()

        if 'key' in r_json:
            context['works_link'] = f"https://openlibrary.org{r_json['key']}"

        if 'title' in r_json:
            context['title'] = r_json['title']

        if 'subtitle' in r_json:
            context['subtitle'] = r_json['subtitle']

        if 'covers' in r_json:
            covers = [cover for cover in r_json['covers'] if cover > 0]
            context['cover'] = covers[0]

        if 'first_publish_date' in r_json:
            context['first_publish_date'] = r_json['first_publish_date']

        if 'subjects' in r_json:
            context['subjects'] = r_json['subjects']

        if 'subject_times' in r_json:
            context['time_period'] = r_json['subject_times']

        if 'authors' in r_json:
            author_keys = [author['author']['key'] for author in r_json['authors']]
            authors = []

            for key in author_keys:
                author_query = f'{API_URL}{key}.json'
                author = requests.get(author_query).json()
                authors.append(author)

            context['authors'] = authors

        if 'description' in r_json:
            description = r_json['description']
            tags = ['([source', '------', '[Source']

            if isinstance(description, dict):
                description = description['value']

            for tag in tags:
                if tag.lower() in description.lower():
                    d_text = description.split(tag)
                    description = d_text[0]

            context['description'] = description

        if 'subject_places' in r_json:
            context['places'] = [place for place in r_json['subject_places']]

        if 'subject_people' in r_json:
            context['characters'] = r_json['subject_people']

        if 'links' in r_json:
            context['links'] = r_json['links']

        return context
