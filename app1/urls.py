from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/authors', views.AuthorsListViewAPI.as_view()),
    path('api/v1/authors/<int:pk>/', views.AuthorsRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/books', views.BooksListViewAPI.as_view()),
    path('api/v1/books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),


]
