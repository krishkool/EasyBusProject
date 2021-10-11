from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from busbookApp.models import Bus

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class SearchBusForm(forms.ModelForm):
    
    source = forms.CharField(label='From',widget=forms.ChoiceField())
    destination = forms.CharField(label='To',widget=forms.ChoiceField())
    date  = forms.DateField(label='Date',widget=forms.DateField())
    class Meta:
        model = User
        fields = ('source', 'destination', 'date')