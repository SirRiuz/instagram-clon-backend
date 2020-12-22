
from django.urls import path
from .views import (ComentsManager,getComentById,SubComentsManager,SubComentsManagerById)

urlpatterns = [
    path('coments/<postId>/post/' , ComentsManager.as_view()),
    path('coments/<comentId>/sub/<subComentId>/' , SubComentsManagerById.as_view()),
    path('coments/<comentId>/sub/' , SubComentsManager.as_view()),
    path('coments/<comentId>/' , getComentById),
]
