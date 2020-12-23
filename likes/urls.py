from django.urls import path,include



# Views
from .views import (createLikeByPost,createLikeByComent)


urlpatterns = [
    path('<str:comentId>/like/coment/',createLikeByComent),
    path('<str:postId>/like/post/',createLikeByPost)
]