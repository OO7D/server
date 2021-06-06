from rest_framework import serializers
from .models import Closet

class ClosetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Closet
        fields = (
            "user",
            "recommendClothes",
            "evaluateRecommend"
            )