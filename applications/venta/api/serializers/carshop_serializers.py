from rest_framework import serializers
from ....venta.models import CarShop

class CarShopSerializers(serializers.ModelSerializer):

    class Meta:
        model = CarShop
        fields = '__all__'