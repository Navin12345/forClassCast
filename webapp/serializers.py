from rest_framework import serializers
from .models import course

class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = fields='__all__'
