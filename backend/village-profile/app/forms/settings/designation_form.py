from django import forms


class DesignationForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required': 'Name is required'})

