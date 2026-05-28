from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
def sample1(request):
    return render(request, 'tasks/t.html', {'name': 'Mahir'})

def sample2(request):
    return render(request, 'tasks/base.html')

def unknown(request):
    messages.success(request, "All Done!!!")
    return HttpResponse("OK")