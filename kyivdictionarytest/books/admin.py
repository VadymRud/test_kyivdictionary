from django.contrib import admin
from .models import Author, Book, BookType, Editor, Interpreter


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(Editor)
admin.site.register(Interpreter)
