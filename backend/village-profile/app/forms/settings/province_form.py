from django import forms


class ProvinceForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required': 'Name is required'})
    code = forms.CharField(max_length=100)
