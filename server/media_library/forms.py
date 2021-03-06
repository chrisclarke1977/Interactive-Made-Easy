from django import forms

class AddMediaForm(forms.Form):
    media_type = forms.ChoiceField(choices=[('image', 'Image'), ('sound', 'Sound'), ('video', 'Video')])
    source = forms.CharField()
    file = forms.FileField(required=False)
    url = forms.CharField(required=False)
