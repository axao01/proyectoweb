from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('Chart/', views.get_chart),
]