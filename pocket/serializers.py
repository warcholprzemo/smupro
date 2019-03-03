from hashlib import sha256

from next_prev import next_in_order, prev_in_order
from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from pocket.models import Blog, SomeData, MyImage


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


class MyImageSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    password = ''

    class Meta:
        model = MyImage
        fields = ('id', 'image', 'size')

    def __init__(self, *args, **kwargs):
        # TODO: Find better way to remove unexpcted value before serialization. Maybe move it to view?
        if 'data' in kwargs:
            data = kwargs['data'].copy()
            self.password = data.pop('magicpassword')
            self.password = self.password[0]
            kwargs['data'] = data
        super().__init__(*args, **kwargs)

    def get_size(self, instance):
        """It is so smart that get_xxx handles xxx field :-)"""
        return [instance.image.width, instance.image.height]


    def create(self, validated_data):
        if sha256(self.password.encode()).hexdigest() != 'eec14b9f0c827323ef4a26ebe4ab3c74fa1e74793fdff374025f21a67a8517d0':
            raise PermissionDenied("Wrong password")
        return super().create(validated_data)
