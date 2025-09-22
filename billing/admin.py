from django.contrib import admin
from .models import Purchase, Subscription


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['id','user','edition','price','status','created_at']
    search_fields = ['user__username','edition__book__title']
    list_filter = ['status','created_at']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','user','plan','starts_at','ends_at','is_active']
    search_fields = ['user__username','plan']
    list_filter = ['plan','is_active']
    date_hierarchy = 'starts_at'