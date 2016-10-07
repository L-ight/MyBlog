from __future__ import unicode_literals

from django.db import models
from DjangoUeditor.models import UEditorField
from Classification import models as Classification_models
from Tag import models as Tag_models
# Create your models here.

class Article(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    created_Datetime = models.DateTimeField(null=True,blank=True,auto_now_add=True)
    updated_Datetime = models.DateTimeField(null=True, blank=True,auto_now=True)
    title = models.CharField(max_length=30)
    summary = models.TextField()
    content = UEditorField('content', height=300, width=1000,
                           default=u'', blank=True, imagePath="uploads/images/",
                           toolbars='besttome', filePath='uploads/files/')

    classification = models.ForeignKey(Classification_models.Classification,null=True,blank=True)
    tag = models.ManyToManyField(Tag_models.Tag,blank=True)

    def __unicode__(self):
        return self.title
