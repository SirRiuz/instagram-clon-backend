from django.urls import path

# Views
from .views import followerManager

urlpatterns = [
    path('followers/', followerManager),
]
