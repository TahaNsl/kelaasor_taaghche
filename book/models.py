from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    logo = models.ImageField(upload_to='publishers/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    authors = models.ManyToManyField(Author, related_name='books', blank=True)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, on_delete=models.SET_NULL, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books', blank=True)
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    isbn = models.CharField(max_length=32, blank=True, db_index=True)
    language = models.CharField(max_length=50)
    page_count = models.PositiveIntegerField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)

    avg_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)
    rating_count = models.PositiveIntegerField(default=0)

    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Edition(models.Model):
    FORMAT_CHOICES = (
        ('ebook', 'E-Book'),
        ('audio', 'Audio Book'),
    )

    book = models.ForeignKey(Book, related_name='editions', on_delete=models.CASCADE)
    format = models.CharField(max_length=20, choices=FORMAT_CHOICES)
    price = models.IntegerField()
    discount_percent = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to='editions/', null=True, blank=True)
    sample_file = models.FileField(upload_to='editions/samples/', null=True, blank=True)
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    filesize_bytes = models.BigIntegerField(null=True, blank=True)
    is_portable = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('book', 'format')

    def discounted_price(self):
        return float(self.price) * (1 - self.discount_percent / 100.0)

    def __str__(self):
        return f"{self.book.title} — {self.format}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user} — {self.book} ({self.rating})"


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='wishlisted_by')
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'book')


class LibraryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='library')
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name='owned_by')
    granted_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'edition')