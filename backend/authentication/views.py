from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

# Create your views here.

class TestView(generics.GenericAPIView):

    def get(self, request):
        return Response({'resp': "It's Working"}, status=status.HTTP_200_OK)