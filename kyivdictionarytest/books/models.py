from django.db import models
import jsonfield


class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    thirdname = models.CharField(max_length=200, null=True, blank=True)


class Editor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    thirdname = models.CharField(max_length=200, null=True, blank=True)


class Interpreter(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    thirdname = models.CharField(max_length=200, null=True, blank=True)

class BookType(models.Model):
    name = models.CharField(max_length=200)


class Book(models.Model):
    author = models.ManyToManyField(Author)
    editor = models.ManyToManyField(Editor, null=True, blank=True)
    interpreter = models.ManyToManyField(Interpreter, null=True, blank=True)
    book_type = models.ManyToManyField(BookType)
    number_pub = models.SmallIntegerField()
    add_info = jsonfield.JSONField(null=True, blank=True)
    pub_date = models.DateField('date published')