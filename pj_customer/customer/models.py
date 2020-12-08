from django.db import models

from postgres_copy import CopyManager
# Create your models here.


class Customer(models.Model):
    """ Class to define database table schema """
    id = models.IntegerField(
        primary_key=True,
        auto_created=False,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    email = models.EmailField(
        max_length=100,
        null=False,
        blank=False,
    )
    gender = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    company = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    city = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    latitude = models.FloatField(
        null=True,
    )
    longitude = models.FloatField(
        null=True,
    )

    objects = CopyManager()

    def __str__(self):
        return f'[{self.id}] {self.first_name} {self.last_name}'
