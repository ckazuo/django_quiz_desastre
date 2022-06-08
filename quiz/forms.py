from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "password")

def save(self, commit=True):
	user = super(NewUserForm, self).save(commit=False)
	user.email = self.cleaned_data['email']
	if commit:
		user.save()
	return user

class addQuestionForm(ModelForm):
	class Meta:
		model=Questionario
		fields="__all__"

class uploadRanking(ModelForm):
	name = forms.TextInput()
	class Meta:
		model = Ranking
		fields = ['username']