from django import forms
from django.forms import ModelForm
from .models import Person


class myForm(forms.Form):
    first_name = forms.CharField(label="fname",max_length=30)
    last_name = forms.CharField(label="lname",max_length=30)
    user_name = forms.CharField(label="username", max_length=30)
    password = forms.CharField(label="pass",max_length=50)
    email = forms.EmailField(label='email',max_length=200)

class myForm2(forms.Form):
    first_name = forms.CharField(label="fname",max_length=30)
    last_name = forms.CharField(label="lname",max_length=30)
    user_name = forms.CharField(label="username", max_length=30)
    password = forms.CharField(label="pass",max_length=50)

class myModelForm(ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'password']