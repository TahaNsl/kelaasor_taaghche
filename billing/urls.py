from django.urls import path
from billing.views import (PurchaseListCreateView, PurchaseRUDView,
                    SubscriptionListCreateView, SubscriptionRUDView)


urlpatterns = [
    path('purchases/', PurchaseListCreateView.as_view(), name='purchase-list-create'),
    path('purchases/<int:pk>/retrieve/', PurchaseRUDView.as_view(), name='purchase-retrieve'),
    path('purchases/<int:pk>/update/', PurchaseRUDView.as_view(), name='purchase-update'),
    path('purchases/<int:pk>/destroy/', PurchaseRUDView.as_view(), name='purchase-destroy'),

    path('subscriptions/', SubscriptionListCreateView.as_view(), name='subscription-list-create'),
    path('subscriptions/<int:pk>/retrieve/', SubscriptionRUDView.as_view(), name='subscription-retrieve'),
    path('subscriptions/<int:pk>/update/', SubscriptionRUDView.as_view(), name='subscription-update'),
    path('subscriptions/<int:pk>/destroy/', SubscriptionRUDView.as_view(), name='subscription-destroy'),
]
