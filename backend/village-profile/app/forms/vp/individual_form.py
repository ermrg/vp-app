from django import forms


class IndividualForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required': 'Name is required'})
