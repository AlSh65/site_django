from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=20, default='BRONZE')
    value = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
class Table(models.Model):
    title = models.CharField(max_length=200)
    old_price = models.SmallIntegerField()
    new_price = models.SmallIntegerField()