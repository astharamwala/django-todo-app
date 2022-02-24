import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def taskList(request):
    return HttpResponse('Sample to do list app')
