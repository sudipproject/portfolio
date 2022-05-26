from django.shortcuts import render
from django.http import HttpResponse

def employeehome(request):
    return render(request,'employee/login.html')
