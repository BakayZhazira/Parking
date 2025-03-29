from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),  # Добавлен слэш
    path('contact/', views.contact, name='contact'),  # Добавлена страница контактов
]
