from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable1":"this is jar",
        "variable2":"this is raj",
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')


def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method =="POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        desc =request.POST.get('desc')
        contact=Contact(name=name ,email=email ,desc=desc ,date=datetime.today())
        contact.save()
        messages.success(request, 'YOUR MESSAGE SENDED SUCCESFULLY !')


    return render(request,'contact.html')
