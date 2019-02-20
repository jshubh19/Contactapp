from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse,Http404,HttpResponseRedirect

from .forms import Contact_form

from django.core.mail import send_mail, get_connection, BadHeaderError
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
    return render(request,'email.html', {'key':form}) #here key is key holding a value (form variable or form value)


def success(request):
    return HttpResponse('Successfully sent your message')