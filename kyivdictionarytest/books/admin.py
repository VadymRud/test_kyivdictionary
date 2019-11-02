from django.contrib import admin
from .models import Author, Book, BookType, Editor, Interpreter


class AuthorAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Fieldset', {'fields':[ 'name', 'surname', 'thirdname', 'initials']}),
    ]
    

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(Editor)
admin.site.register(Interpreter)
