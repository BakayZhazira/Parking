from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):  # Новый обработчик
    return render(request, 'myapp/contact.html')
