from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    registered_by = serializers.ReadOnlyField(source='registered_by.username')
    class Meta:
        model = Item
        fields = '__all__'
