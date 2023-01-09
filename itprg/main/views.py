from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    date = {
        'title': 'Main page',
        'values': ['Some', 'Hello', '123'],
        'obj':{
            'car':'BMW',
            'age': 18,
            'hobby': 'Codding'
        }
    }
    return render(request, 'main/index.html', date)

def about(request):
    return render(request, 'main/about.html')

def home(request):
    return HttpResponse("<ul><li>itpg</li></ul>")