from rest_framework import serializers
from billing.models import Purchase, Subscription


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id','user','edition','price','created_at','status']


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id','user','plan','starts_at','ends_at','is_active']