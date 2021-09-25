from django.urls import path

from core import views

urlpatterns = [
    path('', views.CreateView.as_view()),
    path('write/', views.GetCategory.as_view()),
    path('read/', views.ReadJson.as_view()),
]
