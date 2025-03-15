import json
from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# from django.http import JsonResponse
from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id','title','content','price'])
        data = ProductSerializer(instance).data
        
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
    # return JsonResponse({"message": "Hi there, this is the django API homepage response"})
    return Response(data)

# Create your views here.
