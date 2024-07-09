from rest_framework import serializers
from .models import UmraTour

class UmraTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = UmraTour
        fields = '__all__'
