from __future__ import unicode_literals

from django.db import models

# Create your models here.
from Classification.models import Classification

class Tag(models.Model):
    name = models.CharField(max_length=20)
    classification = models.ForeignKey(Classification)
    summary = models.TextField(null=True,blank=True)
    img = models.ImageField(upload_to='Tag/img',null=True,blank=True)

    def __unicode__(self):
        return self.name