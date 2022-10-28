from rest_framework import serializers
from ....producto.models import Marca

class MarkSerializers(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'