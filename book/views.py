from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from book.models import Category, Author, Publisher, Book, Edition, Review, WishlistItem, LibraryItem
from book.serializers import (CategorySerializer, AuthorSerializer,
                              PublisherSerializer, BookSerializer,
                              EditionSerializer, ReviewSerializer,
                              LibraryItemSerializer, WishlistItemSerializer)


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'parent']
    search_fields = ['name']
    ordering_fields = ['name']


class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categories', 'authors', 'publisher', 'language']
    search_fields = ['title', 'description', 'publisher__name', 'authors__name']
    ordering_fields = ['published_date', 'avg_rating', 'page_count']


class BookRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class EditionListCreateView(ListCreateAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'format', 'is_published']
    search_fields = ['book__title']
    ordering_fields = ['published_date', 'price']


class EditionRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Edition.objects.all()
    serializer_class = EditionSerializer


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book', 'user', 'rating', 'is_approved']
    search_fields = ['user__username', 'book__title', 'body']
    ordering_fields = ['created_at', 'rating']


class ReviewRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class LibraryItemListCreateView(ListCreateAPIView):
    queryset = LibraryItem.objects.all()
    serializer_class = LibraryItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'edition']
    search_fields = ['user__username', 'edition__book__title']
    ordering_fields = ['granted_at', 'expires_at']


class LibraryItemRUDView(RetrieveUpdateDestroyAPIView):
    queryset = LibraryItem.objects.all()
    serializer_class = LibraryItemSerializer


class WishlistItemListCreateView(ListCreateAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'book']
    search_fields = ['user__username', 'book__title']
    ordering_fields = ['added_at']


class WishlistItemRUDView(RetrieveUpdateDestroyAPIView):
    queryset = WishlistItem.objects.all()
    serializer_class = WishlistItemSerializer


class AuthorListCreateView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name', 'bio']
    ordering_fields = ['name']


class AuthorRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherListCreateView(ListCreateAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']


class PublisherRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer