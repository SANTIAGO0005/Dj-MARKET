from rest_framework import serializers
from ...caja.models import CloseBox

class CloseBoxSerializers(serializers.ModelSerializer):

    class Meta:
        model = CloseBox
        fields = '__all__'
