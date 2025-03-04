from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields =['username','first_name','last_name','email']


class ChangeUserDetail(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields =['username','first_name','last_name']

class ChangeAdminDetail(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields ='__all__'