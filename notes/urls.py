from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.NoteListViewAPI.as_view()),
    path('list/<int:pk>/', views.NoteRetrieveUpdateDestroyViewAPI.as_view()),
    path('ws/notes/', views.NoteWebSocketView.as_view()),

]