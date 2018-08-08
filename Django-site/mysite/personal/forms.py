from django import forms

class AddAssetForm(forms.Form):
    file = forms.FileField()


