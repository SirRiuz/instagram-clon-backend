from django.urls import path

# Views
from .views import followerManager,getFollowList


urlpatterns = [
    path('followers/', followerManager),
    path('followers/follows/', getFollowList),
]
