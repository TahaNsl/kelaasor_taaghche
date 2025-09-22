from django.contrib import admin
from django.core.validators import MaxValueValidator, MinValueValidator
from book.models import (Category, Publisher, Book, Edition,
                         Review, Author, LibraryItem, WishlistItem)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent']
    search_fields = ['name']
    list_filter = ['parent']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'website', 'telegram', 'instagram']
    search_fields = ['name']
    list_filter = ['name']
    readonly_fields = ['logo']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher', 'language', 'published_date']
    search_fields = ['title', 'publisher__name', 'authors__name']
    list_filter = ['categories', 'publisher', 'language']
    date_hierarchy = 'published_date'


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'format', 'price', 'discount_percent', 'is_published', 'published_at']
    search_fields = ['book__title']
    list_filter = ['format', 'is_published']
    date_hierarchy = 'published_at'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'rating', 'is_approved', 'created_at']
    search_fields = ['book__title', 'user__username', 'body']
    list_filter = ['is_approved', 'rating', 'created_at']
    date_hierarchy = 'created_at'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'bio']
    search_fields = ['name', 'bio']
    list_filter = ['name']


@admin.register(LibraryItem)
class LibraryItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'edition', 'granted_at', 'expires_at']
    search_fields = ['user__username', 'edition__book__title']
    list_filter = ['granted_at', 'expires_at', 'edition']
    date_hierarchy = 'granted_at'


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'book', 'added_at']
    search_fields = ['user__username', 'book__title']
    list_filter = ['added_at', 'book']
    date_hierarchy = 'added_at'