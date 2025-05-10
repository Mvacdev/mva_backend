from rest_framework import serializers
from apps.core.models import DataHistory, PotentialFranchise, Contact


class DataHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataHistory
        fields = '__all__'


class PotentialFranchiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PotentialFranchise
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
