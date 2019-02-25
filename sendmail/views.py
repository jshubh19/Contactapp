from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,Http404,HttpResponseRedirect

from .forms import Contact_form
#from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, get_connection, BadHeaderError
from django.contrib import messages
from .forms import UserForm
# Create your views here.

def email(request):
    if request.method=='GET':
        form=Contact_form()

    else:
        form=Contact_form(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            try:
                send_mail(name,last_name,email,['abc@gmail.com'],message)
            except BadHeaderError:
                return HttpResponse('Invalid mail or header found.')
            return redirect('success')
    return render(request,'email.html', {'form':form}) #here key is key holding a value (form variable or form value)


def success(request):
    return HttpResponse('Successfully sent your message')




def register(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():

            username=form.cleaned_data.get('username')
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')

            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name,)

      #   messages.success(request,'user create')
            return HttpResponseRedirect('/signup/completed')
    else:
        form=UserForm()
    return render(request,'signup.html')


def regcompleted(request):
    return HttpResponse ("<h3>User created</h3>")