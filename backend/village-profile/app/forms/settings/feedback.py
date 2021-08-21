from django import forms


class FeedbackForm(forms.Form):
    description = forms.CharField(required=True, error_messages={'required': 'Description is required'})
    reporter = forms.CharField(required=True, error_messages={'required': 'Reporter  is required'})


