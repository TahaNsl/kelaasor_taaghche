from django.contrib.auth.models import User
from rest_framework import serializers
from book.models import (Category, Author, Publisher, Book, Edition, Review,
                     WishlistItem, LibraryItem)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','parent','description']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name','bio','photo']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['name','website','logo']


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ['book','format','price','discount_percent','file','sample_file',
                  'duration_seconds','filesize_bytes','is_published','published_at']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    editions = EditionSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['title','description','authors','publisher','categories','cover','isbn',
                  'language','page_count','published_date','avg_rating','rating_count','is_free','editions']


class ReviewSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        # user is temporarily not read-only because we have not implemented login and sign-up yet.
        fields = ['user','book','rating','body','created_at','is_approved']
        read_only_fields = ['created_at','is_approved']


class LibraryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryItem
        fields = ['user', 'edition', 'granted_at', 'expires_at']


class WishlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishlistItem
        fields = ['user', 'book', 'added_at']