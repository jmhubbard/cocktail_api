from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/drink-list/',
        'Detail View': '/drink-detail/<str:pk>/',
        'Create': '/drink-create/',
        'Update': '/drink-update/<str:pk>/',
        'Delete': '/drink-delete/<str:pk>/',
    }
    return Response(api_urls)
