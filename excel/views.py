from django.shortcuts import render

# Create your views here.

def index(request):
    return render('excel/index.html')


def upload(request):
    pass 
