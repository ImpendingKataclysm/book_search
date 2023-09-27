from django import forms


class TitleSearchForm(forms.Form):
    book_title = forms.CharField(max_length=200)
