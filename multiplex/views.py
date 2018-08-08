from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from multiplex.models import Hall, Cinema, CinemaFilter
from multiplex.serializers import CinemaSerializer

class HallList(ListView):
    model = Hall

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['myfilter'] = CinemaFilter(self.request.GET)
        return context


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def cinema_list(request):
    if request.method == 'GET':
        cinemas = Cinema.objects.all()
        serializer = CinemaSerializer(cinemas, many=True)
        #return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        # data = JSONParser().parse(request
        serializer = CinemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #return JsonResponse(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def cinema_detail(request, pk):
#     """
#     Retrieve, update or delete a cinema
#     """
#     try:
#         cinema = Cinema.objects.get(pk=pk)
#     except Cinema.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == "GET":
#         serializer = CinemaSerializer(cinema)
#         return JsonResponse(serializer.data)
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = CinemaSerializer(cinema, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#     elif request.method == "DELETE":
#         cinema.delete()
#         return HttpResponse(status=204)


# use instead rest_framework mixins
from rest_framework import mixins
from rest_framework import generics

class CinemaDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
