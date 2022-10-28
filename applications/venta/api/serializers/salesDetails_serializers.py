from rest_framework import serializers
from ....venta.models import SaleDetail

class SaleDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = SaleDetail
        fields = '__all__'