from rest_framework import viewsets
from . import models
from . import serializer
from rest_framework_api_key.permissions import HasAPIKey

class FlatViewset(viewsets.ModelViewSet):
    queryset = models.Flat.objects.all()
    serializer_class = serializer.FlatSerializer
    permission_classes = [HasAPIKey]

class AgentViewset(viewsets.ModelViewSet):
    queryset = models.Agent.objects.all()
    serializer_class = serializer.AgentSerializer