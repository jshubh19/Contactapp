from django import forms


class Contact_form(forms.Form):
    name=forms.CharField(max_length=10,required=True)
    last_name=forms.CharField(max_length=10,required=True)
    email=forms.EmailField(label='E-mail',required=True)
    category=forms.ChoiceField(choices=[('Question','question'),('other','Other')])
    message=forms.CharField(widget=forms.Textarea,required=True)

    
