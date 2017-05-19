from django import forms


class UrlForm(forms.Form):
    long_url = forms.CharField(label="", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your URL here'}))
    custom_url = forms.CharField(label="", max_length=10, required=False,\
     							widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '*Optional* Enter a max 10 character short link here'}))
