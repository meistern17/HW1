from rest_framework import serializers
from sweets.models import Sweet

class SweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sweet
        fields = ['pk','name', 'brand', 'expiration_date', 'calories']
