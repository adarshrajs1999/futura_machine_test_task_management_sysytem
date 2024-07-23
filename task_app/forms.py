from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from task_app.models import Task


class User_register_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label = "password", widget = forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class Task_form(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('__all__')
        exclude = ('user','completed')

