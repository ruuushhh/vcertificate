from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Profile_form(forms.Form):
    form_f_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    form_l_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    form_email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    form_phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    form_year = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    form_skills = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
