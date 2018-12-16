import random

from rest_framework import generics
from rest_framework.exceptions import APIException

from pocket.models import Blog, SomeData
from pocket.serializers import BlogSerializer, SomeDataSerializer, BlogNextPrevSerializer


class PocketException(APIException):
    status_code = 500
    default_detail = [{"ERROR": "Random 10% probably error"}]


class SomeDataPost(generics.CreateAPIView):
    queryset = SomeData.objects.all()
    serializer_class = SomeDataSerializer


class SomeDataList(generics.ListAPIView):
    queryset = SomeData.objects.all()
    serializer_class = SomeDataSerializer

    def get(self, request, *args, **kwargs):
        if random.random() < 0.1:
            raise PocketException()
        return super().get(request, *args, **kwargs)


class BlogList(generics.ListAPIView):
    queryset = Blog.objects.filter(published=True)
    serializer_class = BlogSerializer


class BlogDetail(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(published=True)
    serializer_class = BlogNextPrevSerializer
