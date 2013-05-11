from django.db import models
from django.contrib import admin


# Create your models here.
class hiddennode(models.Model):
	create_key=models.TextField(editable=False)
        def __unicode__(self):
            return self.create_key



class wordhidden(models.Model):
	fromid=models.PositiveIntegerField(default=10000)
	toid=models.PositiveIntegerField(default=10000)
	strength=models.PositiveIntegerField(default=10000)
	def __unicode__(self):
            return self.fromid


class hiddenurl(models.Model):
	fromid=models.PositiveIntegerField(default=10000)
	toid=models.PositiveIntegerField(default=10000)
	strength=models.PositiveIntegerField(default=10000)
        def __unicode__(self):
            return self.fromid



class HiddenurlAdmin(admin.ModelAdmin):
	list_display=['fromid','toid','strength']

class WordhiddenAdmin(admin.ModelAdmin):
	list_display=['fromid','toid','strength']


class HiddennodeAdmin(admin.ModelAdmin):
	list_display=['create_key']

admin.site.register(hiddenurl,HiddenurlAdmin)
admin.site.register(wordhidden,WordhiddenAdmin)

admin.site.register(hiddennode,HiddennodeAdmin)
