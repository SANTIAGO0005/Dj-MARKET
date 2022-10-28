from rest_framework import viewsets
from ....venta.api.serializers.carshop_serializers import CarShopSerializers

class CarShopViewSet(viewsets.ModelViewSet):
    serializer_class = CarShopSerializers
    queryset = CarShopSerializers.Meta.model.objects.all()
