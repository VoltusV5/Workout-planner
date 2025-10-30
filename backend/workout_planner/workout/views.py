# backend/workout_planner/workout/views.py

from django.http import HttpResponse
from django.conf import settings
import os
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User

# Регистрация
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def create(self, request):
        username = request.data.get('username')
        email = request.data.get('email', '')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password required'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=400)

        User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'User created'}, status=201)

# Текущий пользователь
class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
        })

# SPA
def frontend_view(request):
    index_path = os.path.join(settings.STATIC_ROOT, 'index.html')
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='text/html')
    except FileNotFoundError:
        return HttpResponse("Run: npm run build && collectstatic", status=500)