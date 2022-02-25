from platform import release
from django.db import models


class Network(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tvshows=lista de shows asociados al network


class Tvshow(models.Model):
    title = models.CharField(max_length=100)
    network = models.ForeignKey(Network,
                                related_name="tvshows", on_delete=models.CASCADE)
    releasedate = models.DateField()
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
