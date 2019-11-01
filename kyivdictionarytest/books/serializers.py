from rest_framework import serializers
from .models import Author, Book, BookType, Editor, Interpreter


class AuthorSerializer(serializers.ModelSerializer):
    unique_id = serializers.UUIDField(read_only=False)
    class Meta:
        model = Author
        fields = ['unique_id','name', 'surname', 'thirdname']


class BookTypeSerializer(serializers.ModelSerializer):
    unique_id = serializers.UUIDField(read_only=False)
    class Meta:
        model = BookType
        fields = ['unique_id', 'name']


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

    # def create(self, validated_data):
        
    #     authors = validated_data.pop('authors')
    #     editors = validated_data.pop('editors')
    #     interpreters = validated_data.pop('interpreters')
    #     book_types= validated_data.pop('book_types')

    #     instance = Book.objects.create(**validated_data)
    #     instance.save()
    #     for author in authors:
    #         print(author['unique_id'])
    #         aut = Author.objects.get(unique_id=author['unique_id'])
    #         instance.authors.add(aut)
    #     if editors:
    #         for editor in editors:
    #             instance.editors.add(editor)
    #     if interpreters:
    #         for interpreter in interpreters:
    #             instance.interpreters.add(interpreter)
    
    #     for book_type in book_types:
    #         instance.book_types.add(book_type)
        
    #     return instance
