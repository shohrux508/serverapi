from django.contrib import admin
from django.urls import path, include

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
    path('media/books/<str:file>/', views.FileDownloadViewAPI.as_view()),
]
