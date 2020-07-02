from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    RequestRefundView,
    ItemView,
    ItemCreateView,
    ItemUpdateView,
    ItemDeleteView,
    SellerItemView,

    )

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    ##added
    path('items/<slug:catagory>/<slug:common_name>/', ItemView.as_view(), name='items'),
    path('seller-items/<slug>/', SellerItemView.as_view(), name='seller-items'),

    path('item-add/', ItemCreateView.as_view(), name='add-item'),
    path('item-update/<slug>/', ItemUpdateView.as_view(), name='update-item'),
    path('delete-item/<slug>/', ItemDeleteView.as_view(), name='delete-item'),
]

