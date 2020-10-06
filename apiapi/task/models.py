from django.db import models

class motor(models.Model):
    merek = models.CharField(max_length=200)
    kecepatan = models.DecimalField(default=0, max_digits=10, decimal_places=0)

def __str__(self):
    return '%s %s' % (self.merek, self.kecepatan)