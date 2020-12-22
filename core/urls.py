
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('followers.urls')),
    path('api/v1/', include('post.urls')),
    path('api/v1/', include('coments.urls')),

]
