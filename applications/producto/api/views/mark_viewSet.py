from rest_framework import viewsets
from ....producto.api.serializers.mark_serializer import MarkSerializers

class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializers
    queryset = MarkSerializers.Meta.model.objects.all()