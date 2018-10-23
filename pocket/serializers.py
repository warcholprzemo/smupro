from rest_framework import serializers
from pocket.models import Blog, SomeData


class SomeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomeData
        fields = ('id', 'sometext', 'somenumber', 'somecheckbox')


class BlogSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'
