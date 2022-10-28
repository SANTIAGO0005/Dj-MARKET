from rest_framework import viewsets
from ....users.api.serializers import UserSerializers

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = UserSerializers.Meta.model.objects.all()
