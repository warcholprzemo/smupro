from next_prev import next_in_order, prev_in_order
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


class BlogNextPrevSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = Blog
        fields = '__all__'

    def __serialize_or_None(self, instance):
        if instance:
            return super().to_representation(instance)
        return None

    def to_representation(self, instance):
        queryset = Blog.objects.order_by('id')
        prev_instance = prev_in_order(instance, qs=queryset)
        next_instance = next_in_order(instance, qs=queryset)
        serialized_instance = super().to_representation(instance)
        serialized_prev = self.__serialize_or_None(prev_instance)
        serialized_next = self.__serialize_or_None(next_instance)
        return {
            'instance': serialized_instance,
            'prev_instance': serialized_prev,
            'next_instance': serialized_next,
        }

