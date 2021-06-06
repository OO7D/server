from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "gender",
            "name",
            "age",
            "recentlyRecommended",
            "mostRecommended",
            "mindTestResult",
            "preferenceTestResult"
            )