from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Hiphop.urls')),
    path('', include('Jazz.urls')),
    path('', include('Pop.urls')),
    path('admin/', admin.site.urls),
]
