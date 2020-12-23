

# django
from django.contrib import admin


# models
from .models import (LikePost,LikeComent)



@admin.register(LikeComent)
class LikeComentAdmin(admin.ModelAdmin):
    pass

@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    pass
