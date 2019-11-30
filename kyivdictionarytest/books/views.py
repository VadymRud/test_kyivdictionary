import json
from django.db.models import Q
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorSerializer, BookSerializer, BookTypeSerializer, EditorSerializer, InterpreterSerializer
from .models import Author, Book, BookType, Editor, Interpreter
from .forms import BookForm

class BookList(APIView):

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        serializer = BookSerializer(data=request.data, context={'request':request})
        
        if serializer.is_valid():
            
            
            number_pub = self.request.data.get('number_pub')
            add_info = self.request.data.get('add_info')
            pub_date = self.request.data.get('pub_date')
            city = self.request.data.get('city')
            publisher = self.request.data.get('publisher')
            pages = self.request.data.get('pages')

            instance = Book.objects.create(number_pub=number_pub, add_info=add_info, pub_date=pub_date, city=city,
            publisher=publisher, pages=pages)
            
            authors = self.request.data.get('authors')
            editors = self.request.data.get('editors')
            interpreters = self.request.data.get('interpreters')
            book_types = self.request.data.get('book_types')


            for author in authors:
                aut = Author.objects.get(unique_id=author['unique_id'])
                instance.authors.add(aut)
            
            if editors:
                for editor in editors:
                    ed = Editor.objects.get(unique_id=editor['unique_id'])
                    instance.editors.add(ed)
            if interpreters:
                for interpreter in interpreters:
                    inter = Interpreter.objects.get(unique_id=interpreter['unique_id'])
                    instance.interpreters.add(inter)
        
            for book_type in book_types:
                bt = BookType.objects.get(unique_id=book_type['unique_id'])
                instance.book_types.add(bt)
                # serializer.save()
            bs = BookSerializer(instance).data
            return Response(bs, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookSearh(APIView):

    def get(self, request, string=None, format=None):
        books = Book.objects.filter(Q(authors__name__icontains=string) | Q(authors__surname__icontains=string) | Q(authors__initials__icontains=string))
        bs = BookSerializer(books, many=True).data
        return Response(bs, status=status.HTTP_200_OK)


class BookCreate(CreateView):
    model = Book
    

class BookUpdate(UpdateView):
    model = Book
    

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')