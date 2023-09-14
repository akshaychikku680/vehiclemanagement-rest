from rest_framework import serializers
from .models import Rent
from django.contrib.auth.models import User

class RentSer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)
    vec = serializers.CharField(read_only=True)
    class Meta:
        model = Rent
        fields = "__all__"
