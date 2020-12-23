
from django.urls import path
from .views import (ComentsManager,getComentById,SubComentsManager,SubComentsManagerById)

urlpatterns = [
    path('<postId>/coments/post/' , ComentsManager.as_view()),
    path('<comentId>/coments/sub/<subComentId>/' , SubComentsManagerById.as_view()),
    path('<comentId>/coments/sub/' , SubComentsManager.as_view()),
    path('<comentId>/coments' , getComentById),
]
