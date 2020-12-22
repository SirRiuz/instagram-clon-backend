
# Django
from django.contrib import admin


# Models
from .models import Coment,SubComent



@admin.register(Coment,SubComent)
class ComentAdmin(admin.ModelAdmin):
    pass

