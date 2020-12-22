
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *








class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email', 'password1', 'password2']


class GoalsForm(forms.ModelForm):
	'''goalname= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add a new goal...'}))
	goalstepset=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Targeted number of repetitions...'}))'''

	class Meta:
		model = Goals
		fields = ['goalname','goalstepset']
