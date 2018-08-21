import random

from rest_framework import generics
from rest_framework.exceptions import APIException

from pocket.models import SomeData
from pocket.serializers import SomeDataSerializer


class PocketException(APIException):
    status_code = 500
    default_detail = [{"ERROR": "Random 50% probably error"}]


class SomeDataPost(generics.CreateAPIView):
    queryset = SomeData.objects.all()
    serializer_class = SomeDataSerializer


class SomeDataList(generics.ListAPIView):
    queryset = SomeData.objects.all()
    serializer_class = SomeDataSerializer

    def get(self, request, *args, **kwargs):
        if random.random() > 0.5:
            raise PocketException()
        return super().get(request, *args, **kwargs)
