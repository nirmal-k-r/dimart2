from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.WishlistView.as_view(),name='wishlist'),
]
