from django.db import models
from rest_framework.exceptions import APIException


class SomeNumber55Exception(APIException):
    status_code = 500
    default_detail = "Just cannot save 55 into DB"


class SomeData(models.Model):
    sometext = models.TextField(blank=True)
    somenumber = models.IntegerField(blank=True)
    somecheckbox = models.BooleanField()

    def clean(self):
        if self.somenumber == 55:
            raise SomeNumber55Exception()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)