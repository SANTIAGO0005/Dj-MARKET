from rest_framework import serializers
from ....venta.models import Sale

class SalesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'