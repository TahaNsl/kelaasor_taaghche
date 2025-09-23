from django.urls import path
from book.views import (BookListCreateView, BookRUDView,
                        CategoryListCreateView, CategoryRUDView,
                        ReviewListCreateView, ReviewRUDView,
                        EditionListCreateView, EditionRUDView,
                        LibraryItemListCreateView, LibraryItemRUDView,
                        WishlistItemListCreateView, WishlistItemRUDView,
                        AuthorListCreateView, AuthorRUDView,
                        PublisherListCreateView, PublisherRUDView, book_list_html)

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookRUDView.as_view(), name='book-rud'),
    path("html/", book_list_html, name="book-list-html"),

    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRUDView.as_view(), name='author-rud'),

    path('publishers/', PublisherListCreateView.as_view(), name='publisher-list-create'),
    path('publishers/<int:pk>/', PublisherRUDView.as_view(), name='publisher-rud'),

    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRUDView.as_view(), name='category-rud'),

    path('editions/', EditionListCreateView.as_view(), name='edition-list-create'),
    path('editions/<int:pk>/', EditionRUDView.as_view(), name='edition-rud'),

    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRUDView.as_view(), name='review-rud'),

    path('library-items/', LibraryItemListCreateView.as_view(), name='libraryitem-list-create'),
    path('library-items/<int:pk>/', LibraryItemRUDView.as_view(), name='libraryitem-rud'),

    path('wishlist-items/', WishlistItemListCreateView.as_view(), name='wishlistitem-list-create'),
    path('wishlist-items/<int:pk>/', WishlistItemRUDView.as_view(), name='wishlistitem-rud'),
]