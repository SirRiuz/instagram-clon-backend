
# Django
from django.contrib import admin


# Models 
from .models import Followers


@admin.register(Followers)
class FollowerAdmin(admin.ModelAdmin):
    pass