from rest_framework import serializers
from . import models

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flat
        fields = ('id', 'code', 'url', 'title', 'rooms', 'price')

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Agent
        fields = ('id', 'first_name', 'last_name')