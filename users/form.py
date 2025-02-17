from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'required'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']
        # fields = '__all__'
        