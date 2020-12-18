from django.urls import path

# Views
from .views import (
    PostManager,
    getPostByFollower,
    PostManagerById
)


urlpatterns = [
    path('post/', PostManager.as_view()),
    path('post/follow/',getPostByFollower.as_view()),
    path('post/<str:id>/', PostManagerById.as_view()),
]
