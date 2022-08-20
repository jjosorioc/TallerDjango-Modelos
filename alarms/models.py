from django.db import models
from measurements.models import Measurement


class Alarm(models.Model):
    name = models.CharField(max_length=20)
    measurements = models.ManyToManyField(Measurement,verbose_name="measurements")
    
    def __str__(self) -> str:
        return "{0}: {1}".format(self.name, repr(self.measurements.all()))