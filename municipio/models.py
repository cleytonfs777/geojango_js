# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models


class Municipio(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name

