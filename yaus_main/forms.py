from django import forms


class UrlForm(forms.Form):
    long_url = forms.CharField(label="", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
