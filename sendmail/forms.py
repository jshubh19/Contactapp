from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Contact_form(forms.Form):
    name=forms.CharField(max_length=10,required=True)
    last_name=forms.CharField(max_length=10,required=True)
    email=forms.EmailField(label='E-mail',required=True)
    category=forms.ChoiceField(choices=[('Question','question'),('other','Other')])
    message=forms.CharField(widget=forms.Textarea,required=True)

    
class UserForm(forms.Form):

    class Meta:
        model= User
        fields='__all__'
