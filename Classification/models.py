from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Classification(models.Model):
    name = models.CharField(max_length=20)
    summary = models.TextField()
    img = models.ImageField(upload_to='Classification/img')

    def __unicode__(self):
        return self.name
