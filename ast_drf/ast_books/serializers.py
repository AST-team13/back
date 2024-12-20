from rest_framework import serializers
from .models import Review, Book, BookPicture, AudioFile


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'text', 'author', 'price_url']


class BookPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPicture
        fields = ['id', 'title', 'image', 'book']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author', 'create', 'text', 'pros']


class ReviewPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookPicture
        fields = ['id', 'title', 'image']


class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields = ['id', 'title', 'audio_file']
