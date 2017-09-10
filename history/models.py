from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class History(models.Model):
    title = models.CharField(max_length = 100, verbose_name = u'标题')
    body = RichTextUploadingField(config_name = 'awesome_ckeditor', verbose_name = u'内容')
    time = models.DateField(auto_now_add = True)

    def __str__(self):
        return 'title = %s, time = %s' % (self.title, self.time)
    class Meta:
        verbose_name_plural = verbose_name = u'历届文章'
