from rest_framework import viewsets
from ...caja.api.serializers import CloseBoxSerializers


class CloseBoxViewSet(viewsets.ModelViewSet):
    serializer_class = CloseBoxSerializers
    queryset = CloseBoxSerializers.Meta.model.objects.all()
