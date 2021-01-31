from django.urls import path,include



# Views
from .views import (
    createLikeByPost,
    createLikeByComent,
    createLikeBySubComent
)


urlpatterns = [
    path('<str:comentId>/like/coment/sub/<str:subComentId>/',createLikeBySubComent),
    path('<str:comentId>/like/coment/',createLikeByComent),
    path('<str:postId>/like/post/',createLikeByPost)
]