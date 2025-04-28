from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import ChatForm


def index(request):
    return render(request, 'myapp/index.html')


def about(request):
    return render(request, 'myapp/about.html')
