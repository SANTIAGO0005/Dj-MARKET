from rest_framework import viewsets
from ....producto.api.serializers.provider_serializer import ProviderSerializers

class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializers
    queryset = ProviderSerializers.Meta.model.objects.all()