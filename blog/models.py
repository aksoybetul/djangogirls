from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Post(models.Model):
    yazar = models.ForeignKey('auth.User')
    baslik = models.CharField(max_length=200)
    yazi = models.TextField()
    yaratilma_tarihi = models.DateTimeField(
           default=timezone.now)
    yayinlanma_tarihi = models.DateTimeField(
           blank=True, null=True)
    colour = models.CharField(max_length=50, default="purple")


    def yayinla(self):
        self.yayinlanma_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.baslik
