from django import forms


class FiscalYearForm(forms.Form):
    year = forms.CharField(required=True, error_messages={'required': 'Year is required'})
