from rest_framework import serializers
from .models import Author, Book, BookType, Editor, Interpreter


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'surname', 'thirdname']


class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields = ['name']


class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editor
        fields = ['name', 'surname', 'thirdname']


class InterpreterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpreter
        fields = ['name', 'surname', 'thirdname']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    editor = EditorSerializer(many=True, required=False)
    interpreter = InterpreterSerializer(many=True, required=False)
    book_type = BookTypeSerializer(many=True)
    class Meta:
        model = Book
        fields = ['author', 'editor', 'interpreter', 'book_type', 'number_pub', 'add_info', 'pub_date']

    def create(self, validated_data):
        
        return Book.objects.create(**validated_data)
