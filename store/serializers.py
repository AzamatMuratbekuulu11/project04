from rest_framework import serializers
from .models import *

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = 'id', 'title_name', 'published_date', 'pages', 'image', 'have'

