
# Django
from django.contrib import admin


# Models
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
