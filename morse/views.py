from django.shortcuts import render
from django.http import HttpResponse

def morse(request):
    return render(request, 'morse/morse.html')