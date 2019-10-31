from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer, BookTypeSerializer, EditorSerializer, InterpreterSerializer
from .models import Author, Book, BookType, Editor, Interpreter


class UserViewSet(viewsets.ModelViewSet):
   
    queryset = Book.objects.all()
    serializer_class = BookSerializer
