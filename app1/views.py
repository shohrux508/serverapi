import rest_framework.views
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models
from . import serializers


# Create your views here.

class AuthorsCreateViewAPI(generics.CreateAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BooksCreateViewAPI(generics.CreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.AuthorSerializer()


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


# search

class AuthorsSearchViewAPI(generics.ListAPIView):
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self):
        gender = self.request.query_params.get('gender')
        bio = self.request.query_params.get('bio')
        age = self.request.query_params.get('age')
        name = self.request.query_params.get('name')
        queryset = models.Author.objects.all()
        if gender:
            queryset = queryset.filter(gender=gender)
        elif bio:
            queryset = queryset.filter(bio=bio)
        elif age:
            queryset = queryset.filter(age=age)
        elif name:
            queryset = queryset.filter(name=name)
        return queryset

class BooksSearchViewAPI(generics.ListAPIView):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title')
        queryset = models.Book.objects.all()
        if title:
            queryset = queryset.filter(title=title)
        return queryset
