from django.shortcuts import render
from rest_framework import generics

from tictactoe.models import TicTacToe
from tictactoe.serializers import TicTacToeSerializer


class SaveResult(generics.CreateAPIView):
    queryset = TicTacToe.objects.all()
    serializer_class = TicTacToeSerializer
