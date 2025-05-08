from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        # Placeholder for registration logic
        return Response({'message': 'User registered successfully!'}, status=status.HTTP_201_CREATED)
