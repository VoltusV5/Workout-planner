# backend/workout_planner/workout_planner/urls.py

from django.contrib import admin
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from workout.views import RegisterView, UserView, frontend_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/user/', UserView.as_view(), name='current-user'),

    # SPA
    re_path(r'^.*$', frontend_view),
]