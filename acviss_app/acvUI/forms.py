from django import forms


class NumberForm(forms.Form):
    number_of_codes = forms.IntegerField()
    batch_name = forms.CharField(max_length=100)

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)
