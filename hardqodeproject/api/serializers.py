from rest_framework import serializers
from main.models import Product, Products_Access, Lesson

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"