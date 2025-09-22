from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Purchase, Subscription
from .serializers import PurchaseSerializer, SubscriptionSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PurchaseListCreateView(ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','status']
    search_fields = ['user__username', 'edition__book__title']
    ordering_fields = ['created_at', 'price']


class PurchaseRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class SubscriptionListCreateView(ListCreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user','plan','is_active']
    search_fields = ['user__username', 'plan']
    ordering_fields = ['starts_at', 'ends_at']


class SubscriptionRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer