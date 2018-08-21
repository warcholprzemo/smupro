from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import APIException

from tictactoe.models import TicTacToe
from tictactoe.serializers import TicTacToeSerializer


class TicTacException(APIException):
    status_code = 404
    default_detail = [{"ERROR": "This view is not ready yet"}]


class SaveResult(generics.CreateAPIView):
    queryset = TicTacToe.objects.all()
    serializer_class = TicTacToeSerializer


class ListResult(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        raise TicTacException
