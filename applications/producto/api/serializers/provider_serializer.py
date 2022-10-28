from rest_framework import serializers
from ....producto.models import Provider

class ProviderSerializers(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'