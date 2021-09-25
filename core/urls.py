from django.urls import path

from core import views

urlpatterns = [
    path('create_contract/', views.CreateContract.as_view()),
    path('create_cte/', views.CreateCTE.as_view()),
    path('write/', views.GetCategory.as_view()),
    path('read/', views.ReadJson.as_view()),
]
