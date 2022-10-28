from rest_framework import viewsets
from ....venta.api.serializers.sales_serializers import SalesSerializers

class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SalesSerializers
    queryset = SalesSerializers.Meta.model.objects.all()