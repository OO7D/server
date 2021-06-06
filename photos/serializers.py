from rest_framework import serializers
from .models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = (
                "user",
                "closet",
                "types",
                "color",
                "season",
                "photo",
                "heart"
            )