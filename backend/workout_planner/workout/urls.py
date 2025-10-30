# workout/urls.py
from django.urls import path
from .views import (
    RegisterView, UserView, frontend_view,
    ExerciseListCreateView, ExerciseRetrieveUpdateDestroyView,
    WorkoutListCreateView, WorkoutRetrieveUpdateDestroyView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserView.as_view(), name='current-user'),

    # УПРАЖНЕНИЯ
    path('exercises/', ExerciseListCreateView.as_view(), name='exercise-list'),
    path('exercises/<int:pk>/', ExerciseRetrieveUpdateDestroyView.as_view(), name='exercise-detail'),

    # ТРЕНИРОВКИ
    path('workouts/', WorkoutListCreateView.as_view(), name='workout-list'),
    path('workouts/<int:pk>/', WorkoutRetrieveUpdateDestroyView.as_view(), name='workout-detail'),
]