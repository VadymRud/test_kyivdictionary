from django import forms
from .models import Author, Book, BookType, Editor, Interpreter


class BookForm(forms.Form):
    
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
    editors = forms.ModelMultipleChoiceField(queryset=Editor.objects.all(), null=True, blank=True)
    interpreters = forms.ModelMultipleChoiceField(queryset=Interpreter.objects.all(), null=True, blank=True)
    book_types  = forms.ModelMultipleChoiceField(queryset=BookType.objects.all())
    number_pub = forms.IntegerField()
    
    pub_date = forms.DateField()
    city = forms.CharField(max_length=200)
    publisher = forms.CharField(max_length=200)
    pages = forms.IntegerField()
