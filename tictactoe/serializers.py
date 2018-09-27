from rest_framework import serializers

from tictactoe.models import TicTacToe, RESULT_CHOICES


class TicTacToeSerializer(serializers.ModelSerializer):
    game_date = serializers.DateTimeField(format='%Y-%m-%d %H:%M', read_only=True)

    class Meta:
        model = TicTacToe
        fields = ('id', 'playerX', 'playerO', 'result', 'game_date')
        read_only_fields = ('id', 'game_date')

    def to_representation(self, instance):
        choices = dict(RESULT_CHOICES)
        instance.result = choices[instance.result]
        return super().to_representation(instance)