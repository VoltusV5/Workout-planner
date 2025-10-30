# workout/views.py

import os
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Exercise, Workout
from .serializers import ExerciseSerializer, WorkoutSerializer


# === РЕГИСТРАЦИЯ ===
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email', '')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password required'}, status=400)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'User already exists'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'User created successfully', 'id': user.id}, status=201)


# === ТЕКУЩИЙ ПОЛЬЗОВАТЕЛЬ ===
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email or '',
        })


# === SPA (Vue) ===
def frontend_view(request):
    index_path = os.path.join(settings.STATICFILES_DIRS[0] if settings.DEBUG else settings.STATIC_ROOT, 'index.html')
    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            return HttpResponse(f.read(), content_type='text/html')
    except FileNotFoundError:
        return HttpResponse(
            "Error: Frontend not built. Run: <code>npm run build && python manage.py collectstatic</code>",
            status=500
        )


# === ПРОВЕРКА ВЛАДЕНИЯ ===
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


# === УПРАЖНЕНИЯ ===
class ExerciseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExerciseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        return Exercise.objects.filter(user=self.request.user)


# === ТРЕНИРОВКИ ===
class WorkoutListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class WorkoutRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)