# backend/workout_planner/workout_planner/urls.py

from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


from workout.views import (
    RegisterView, UserView, frontend_view,
    ExerciseListCreateView, ExerciseRetrieveUpdateDestroyView,
    WorkoutListCreateView, WorkoutRetrieveUpdateDestroyView
)
urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/user/', UserView.as_view(), name='current-user'),

    # УПРАЖНЕНИЯ
    path('api/exercises/', ExerciseListCreateView.as_view(), name='exercise-list'),
    path('api/exercises/<int:pk>/', ExerciseRetrieveUpdateDestroyView.as_view(), name='exercise-detail'),

    # ТРЕНИРОВКИ
    path('api/workouts/', WorkoutListCreateView.as_view(), name='workout-list'),
    path('api/workouts/<int:pk>/', WorkoutRetrieveUpdateDestroyView.as_view(), name='workout-detail'),

    # SPA
    re_path(r'^.*$', frontend_view),
]


# МЕДИА
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)