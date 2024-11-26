from rest_framework import serializers

from .models import *


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class AuthorListSerializer(serializers.ModelSerializer):
    """Вывод списка авторов"""

    class Meta:
        model = Author
        fields = ("id", "name")


class BookListSerializer(serializers.ModelSerializer):
    """Список книг"""
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()

    class Meta:
        model = Book
        fields = ("id", "title", "isbn", "rating_user", "middle_star", "poster")


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("id", "name", "text", "children")


class BookDetailSerializer(serializers.ModelSerializer):
    """Полная книга"""
    author = AuthorListSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        exclude = ("draft",)


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""

    class Meta:
        model = Rating
        fields = ("star", "movie")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            movie=validated_data.get('movie', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating
