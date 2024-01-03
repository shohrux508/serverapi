from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from . import models
from . import paginators
from . import serializers


# Create your views here.

class AuthorsCreateViewAPI(generics.CreateAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookReviewCreateViewAPI(generics.CreateAPIView):
    queryset = models.BookReview.objects.all()
    serializer_class = serializers.BookReviewSerializer


class BooksCreateViewAPI(generics.CreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class AuthorsListViewAPI(generics.ListAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    pagination_class = paginators.AuthorsListPaginators


class BookReviewListViewAPI(generics.ListAPIView):
    queryset = models.BookReview.objects.all()
    serializer_class = serializers.BookReviewSerializer
    pagination_class = paginators.ReviewListPaginator


class AuthorsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer
    permission_classes = (IsAuthenticated,)


class BookReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.BookReview.objects.all()
    serializer_class = serializers.BookReviewSerializer


class BooksListViewAPI(generics.ListAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    pagination_class = paginators.BooksListPaginator


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


class BookReviewSearchViewAPI(generics.ListAPIView):
    serializer_class = serializers.BookReviewSerializer

    def get_queryset(self):
        grade = self.request.query_params.get('grade')
        book = self.request.query_params.get('book')
        author = self.request.query_params.get('author')
        queryset = models.BookReview.objects.all()
        if grade:
            queryset = queryset.filter(grade=grade)
        elif book:
            queryset = queryset.filter(book=book)
        elif author:
            queryset = queryset.filter(author=author)
        return queryset

