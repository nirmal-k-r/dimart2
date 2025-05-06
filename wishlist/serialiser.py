from .models import Wishlist
from rest_framework import serializers

class WishlistSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'