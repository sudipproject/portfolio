from django.shortcuts import render
from django.http import HttpResponse

def employeehome(request):
    return HttpResponse('This is employee home page')
