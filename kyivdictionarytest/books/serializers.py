from rest_framework import serializers
from .models import Author, Book, BookType, Editor, Interpreter


class AuthorSerializer(serializers.ModelSerializer):
    unique_id = serializers.UUIDField(read_only=False)
    class Meta:
        model = Author
        fields = ['unique_id','name', 'surname', 'thirdname', 'initials']


class BookTypeSerializer(serializers.ModelSerializer):
    unique_id = serializers.UUIDField(read_only=False)
    class Meta:
        model = BookType
        fields = ['unique_id', 'name', 'short_name']


class EditorSerializer(serializers.ModelSerializer):
    unique_id = serializers.UUIDField(read_only=False)
    class Meta:
        model = Editor
        fields = ['unique_id', 'name', 'surname', 'thirdname']


class InterpreterSerializer(serializers.ModelSerializer):
    unique_id = serializers.UUIDField(read_only=False)
    class Meta:
        model = Interpreter
        fields = ['unique_id', 'name', 'surname', 'thirdname']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    editors = EditorSerializer(many=True, required=False )
    interpreters = InterpreterSerializer(many=True, required=False)
    book_types = BookTypeSerializer(many=True)
    class Meta:
        model = Book
        fields = ['id', 'authors', 'editors', 'interpreters', 'book_types', 'number_pub', 'add_info', 'pub_date', 'city', 'publisher', 'pages']

    