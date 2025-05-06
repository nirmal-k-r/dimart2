from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.contrib.auth.models import User #use the default user models

class AuthenticationSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('username','password')

    