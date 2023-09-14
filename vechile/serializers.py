from rest_framework import serializers
from .models import Vechile
from django.contrib.auth.models import User


class SignUpSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","username","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class VechileSerializer(serializers.ModelSerializer):
    availability = serializers.BooleanField(read_only=True)
    class Meta:
        model = Vechile
        fields = "__all__"