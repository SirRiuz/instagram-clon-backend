

from django.urls import path,include


# Views
from .views import (auth,register,authSocial)

urlpatterns = [
    path('accounts/auth/' , auth),
    path('accounts/register/' , register),
    path('accounts/auth/social/' , authSocial)
]