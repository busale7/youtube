from django import forms
from django.contrib.auth.models import User
from .models import Video, Channel

class ChannelForm(forms.ModelForm):
	class Meta: 
		model= Channel
		fields = '__all__'
class VideoForm(forms.ModelForm):
	class Meta:
		model= Video 
		fields ='__all__'

class SignupForm(forms.ModelForm):
	class Meta:
		model=User
		fields =['username','email','first_name','last_name','password']
		widgets={
			"password": forms.PasswordInput()
		}
class LoginForm(forms.ModelForm):
	username=forms.CharField(required=True)
	password =forms.CharField(required=True, widget=forms.PasswordInput())

