from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('notes/', include('notes.urls')),
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
]
