from rest_framework import serializers
from pocket.models import SomeData


class SomeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeData
        fields = ('id', 'sometext', 'somenumber', 'somecheckbox')
