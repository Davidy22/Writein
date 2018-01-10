from django import forms
from django.core.exceptions import ValidationError

class newPollForm(forms.Form):
	questionField = forms.CharField()

	def __init__(self, *args, **kwargs):
		super(newPollForm, self).__init__(*args, **kwargs)
		self.fields['questionField'].label = False

	def clean_questionField(self):
		data = self.cleaned_data['questionField']
		return data #clean later


class submitEntryForm(forms.Form):
	entryField = forms.CharField()

	def __init__(self, *args, **kwargs):
		super(submitEntryForm, self).__init__(*args, **kwargs)
		self.fields['entryField'].label = False

	def clean_entryField(self):
		data = self.cleaned_data['entryField']
		return data #clean later
