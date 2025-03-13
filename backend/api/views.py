from django.shortcuts import render
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hi there, this is the django API homepage response"})

# Create your views here.
