from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def manager_home(request):
    return render(request,'mess_app/mess.html')