from django import forms


class AddingForm(forms.Form):
    description = forms.CharField(max_length=1024)
