from rest_framework import viewsets
from ....venta.api.serializers.salesDetails_serializers import SaleDetailSerializers

class SaleDetailViewSet(viewsets.ModelViewSet):
    serializer_class = SaleDetailSerializers
    queryset = SaleDetailSerializers.Meta.model.objects.all()