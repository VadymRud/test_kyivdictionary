from django.db import models
import jsonfield
import uuid


class Author(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    thirdname = models.CharField(max_length=200, null=True, blank=True)
    initials = models.CharField(max_length=200, null=True, blank=True) 

class Editor(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    thirdname = models.CharField(max_length=200, null=True, blank=True)


class Interpreter(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    thirdname = models.CharField(max_length=200, null=True, blank=True)

class BookType(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=200)


class Book(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    authors = models.ManyToManyField(Author)
    editors = models.ManyToManyField(Editor, null=True, blank=True)
    interpreters = models.ManyToManyField(Interpreter, null=True, blank=True)
    book_types  = models.ManyToManyField(BookType)
    number_pub = models.SmallIntegerField()
    add_info = jsonfield.JSONField(null=True, blank=True)
    pub_date = models.DateField('date published')
    city = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    pages = models.IntegerField()
    