from django import forms

MAX_FIELD_LEN = 200


class SearchForm(forms.Form):
    book_title = forms.CharField(
        max_length=MAX_FIELD_LEN,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Title',
            'class': 'form-control'
        })
    )
    author_name = forms.CharField(
        max_length=MAX_FIELD_LEN,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Author',
            'class': 'form-control'
        })
    )
    subject_keyword = forms.CharField(
        max_length=MAX_FIELD_LEN,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Subject',
            'class': 'form-control'
        })
    )
