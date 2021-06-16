from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def apiList(request):
    return JsonResponse("API List", safe=False)
