from rest_framework import serializers
from .models import Car

class CarTelematicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'  # Or specify the fields you want to serialize
