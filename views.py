from django.shortcuts import render
from .models import MyModel

def home(request):
    return render(request, 'home.html', {'message': 'Hello, Django!'})

def detail(request, pk):
    item = MyModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'item': item})