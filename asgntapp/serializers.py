from rest_framework import serializers
from .models import Office
from dataclasses import fields
class OfficeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'