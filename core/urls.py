from django.urls import path

from core import views

urlpatterns = [
    path('', views.CreateView.as_view()),
]
