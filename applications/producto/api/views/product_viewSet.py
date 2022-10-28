from rest_framework import viewsets
from ....producto.api.serializers.product_serializer import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = ProductSerializers.Meta.model.objects.all()