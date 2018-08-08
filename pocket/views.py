from rest_framework import generics

from pocket.models import SomeData
from pocket.serializers import SomeDataSerializer

class SomeDataPost(generics.CreateAPIView):
    queryset = SomeData.objects.all()
    serializer_class = SomeDataSerializer


class SomeDataList(generics.ListAPIView):
    queryset = SomeData.objects.all()
    serializer_class = SomeDataSerializer
