from rest_framework import serializers
from apps.core.models import DataHistory, PotentialFranchise


class DataHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataHistory
        fields = '__all__'


class PotentialFranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialFranchise
        fields = '__all__'
