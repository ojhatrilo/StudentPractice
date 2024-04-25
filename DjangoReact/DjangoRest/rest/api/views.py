from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def api(request):
    route = [
        {
            'id':1,
            'name':'John Doe',
            'age':30,
            'gender':'Male'
        },
        {
            'id':2,
            'name':'Jane Doe',
            'age':25,
            'gender':'Female'
        },
        {
            'id':3,
            'name':'Tom Smith',
            'age':45,
            'gender':'Male'
        }
    
    ]
    return Response(route)
