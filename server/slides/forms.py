from django import forms
from django.forms.widgets import HiddenInput

class SlideForm(forms.Form):
    name = forms.CharField()
    #media_name = forms.CharField(widget=HiddenInput())
    html = forms.CharField()
