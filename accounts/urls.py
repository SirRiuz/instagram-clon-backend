

from django.urls import path,include


# Views
from .views import (auth,register)

urlpatterns = [
    path('accounts/auth/' , auth),
    path('accounts/register/' , register)
]