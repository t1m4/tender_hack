from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import CTE
from services.data.read import save_cte
from django.conf import settings

from services.data.json_service import write_json, read_json


class CreateView(APIView):
    def get(self,request):
        filename = settings.BASE_DIR / 'services/data/CTE.xlsx'
        # filename = settings.BASE_DIR / 'services/data/cte_test.xlsx'
        # read_cte(filename)
        return Response('ok')

class GetCategory(APIView):
    def get(self,request):
        # category = CTE.objects.filter().annotate(Count('category',distinct=True))
        category = CTE.objects.filter().values('category').distinct()

        # print(category.count())
        # print(category)
        categories = [i.get('category') for i in category]
        # print(categories[:10])
        write_json('categories.json', categories)
        return Response('ok')

class ReadJson(APIView):
    def get(self,request):
        # category = CTE.objects.filter().annotate(Count('category',distinct=True))
        category = CTE.objects.filter().values('category').distinct()

        # print(category.count())
        # print(category)
        categories = [i.get('category') for i in category]
        # print(categories[:10])
        # write_json('categories.json', category[:10])
        result = read_json('categories.json')
        return Response(result)
