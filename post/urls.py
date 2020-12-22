from django.urls import path

# Views
from .views import (
    PostManager,
    getPostByFollower,
    PostManagerById
)


urlpatterns = [
    path('post/', PostManager.as_view()),
    path('follow/post/',getPostByFollower.as_view()),
    path('<str:id>/post/', PostManagerById.as_view()),
]
