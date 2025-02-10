from rest_framework import serializers
from apps.core.models import DataHistory


class DataHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataHistory
        fields = '__all__'

