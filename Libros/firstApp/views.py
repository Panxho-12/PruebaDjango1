from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def renderTemplate(request):
    return render(request, 'firstTemplate/templade1.html')
