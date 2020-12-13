

from django.urls import path,include


# Views
from .views import auth

urlpatterns = [
    path('accounts/auth/' , auth)
]