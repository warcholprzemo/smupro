from django.db import models

RESULT_CHOICES = (
    (-1, "X won"),
    (0,  "Tie"),
    (1,  "O won"),
)


class TicTacToe(models.Model):
    game_date = models.DateTimeField(auto_now_add=True)
    playerX = models.CharField(max_length=100)
    playerO = models.CharField(max_length=100)
    result = models.IntegerField(choices=RESULT_CHOICES)
