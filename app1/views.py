from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


# Create your views here.


class AuthorsListViewAPI(generics.ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class AuthorsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = (IsAuthenticated,)


class BooksListViewAPI(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    permission_classes = (IsAuthenticated,)


def welcome(request):
    print(request)
    print("Hello World")

