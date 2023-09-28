from django import forms

MAX_FIELD_LEN = 200


class TitleSearchForm(forms.Form):
    book_title = forms.CharField(max_length=MAX_FIELD_LEN, required=False)
    author_name = forms.CharField(max_length=MAX_FIELD_LEN, required=False)
    subject_keyword = forms.CharField(max_length=MAX_FIELD_LEN, required=False)
