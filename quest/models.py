from django.db import models
from django.contrib.postgres.fields import ArrayField


class Channel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    bid_types = ArrayField(models.CharField(max_length=3))

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    channel = models.ForeignKey('Channel')
    bid = models.FloatField()
    bid_type = models.CharField(max_length=3)

    def __str__(self):
        return self.name
