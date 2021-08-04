from rest_framework import serializers
from django.core.validators import RegexValidator

from .models import ComputerModel

class ComputerSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(validators=[
        RegexValidator('^[a-zA-Z]{2,20}$', 'only alpha min 2ch max 20ch')
    ])
    ram = serializers.IntegerField(min_value=0)
    processor = serializers.FloatField(min_value=0)
    monitor = serializers.FloatField(min_value=0)
    class Meta:
        model = ComputerModel
        fields = '__all__'
