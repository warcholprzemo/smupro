from rest_framework import serializers

from tictactoe.models import TicTacToe


class TicTacToeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicTacToe
        fields = ('playerX', 'playerO', 'result')
