from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from services.data.read import read_cte
from django.conf import settings

class CreateView(APIView):
    def get(self,request):
        filename = settings.BASE_DIR / 'services/data/CTE.xlsx'
        filename = settings.BASE_DIR / 'services/data/cte_test.xlsx'
        read_cte(filename)
        return Response('ok')
