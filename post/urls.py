from django.urls import path

# Views
from .views import (
    getPostByNickName,
    getPostByFollower
)


urlpatterns = [
    path('post/', getPostByNickName.as_view()),
    path('post/follow/',getPostByFollower.as_view())
]
