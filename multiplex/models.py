from django.core.exceptions import ValidationError
from django.db import models
import django_filters
from pygments.lexers import get_all_lexers


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])

class Cinema(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    open_time = models.TimeField(null=True)
    close_time = models.TimeField(null=True)
    active = models.BooleanField()
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kina"

    def __str__(self):
        return f"({self.id}){self.name}"


class CinemaFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Cinema
        fields = ['open_time', 'active']


class Hall(models.Model):
    cinema = models.ForeignKey(Cinema, null=False, on_delete=models.PROTECT)
    standard_places = models.PositiveIntegerField(blank=False, null=False)
    vip_places = models.PositiveIntegerField(blank=False, null=False)
    number = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        verbose_name = "Sala kinowa"
        verbose_name_plural = "Sale kinowe"

    def __str__(self):
        return f"{self.id}) #Kino: {self.cinema} #Sala: {self.number}"
