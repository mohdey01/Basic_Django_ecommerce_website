from django.http import HttpResponse
from django.shortcuts import render

def Index(request):
    return render(request,"HomePage.html")