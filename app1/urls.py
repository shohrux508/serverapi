from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/authors', views.AuthorsListViewAPI.as_view()),
    path('api/v1/authors/new', views.AuthorsCreateViewAPI.as_view()),
    path('api/v1/authors/<int:pk>/', views.AuthorsRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/books', views.BooksListViewAPI.as_view()),
    path('api/v1/books/new', views.BooksCreateViewAPI.as_view()),
    path('api/v1/books/<int:pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/authors/search/', views.AuthorsSearchViewAPI.as_view()),
    path('api/v1/books/search/', views.BooksSearchViewAPI.as_view()),




]
