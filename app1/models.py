import uuid

from django.db import models


# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    genders = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(choices=genders, max_length=15)
    age = models.CharField(max_length=15)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/books')
    link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
