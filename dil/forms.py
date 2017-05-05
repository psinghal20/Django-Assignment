from django import forms

class Login(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20,widget = forms.PasswordInput)

class Register(forms.Form):
	username = forms.CharField(max_length=20)
	password = forms.CharField(max_length=20,widget=forms.PasswordInput)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=20)
	last_name = forms.CharField(max_length=20)
	branch = forms.CharField()
	dob = forms.DateField()
	year = forms.IntegerField()

class SendMessage(forms.Form):
	message = forms.CharField(max_length=1000,widget=forms.Textarea)