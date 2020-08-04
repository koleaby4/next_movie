from django.shortcuts import render, HttpResponse, render

def index(request):
    return render(request, 'index.html')
