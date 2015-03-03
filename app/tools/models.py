import os
from django.db import models
from django.conf import settings
from translatable.models import TranslatableModel, get_translation_model
import storages.backends.s3boto
from django.utils.deconstruct import deconstructible

@deconstructible
class MyS3BotoStorage(storages.backends.s3boto.S3BotoStorage):
    # subclass fixed to allow migrations
    pass



PSYTOOLS_WORKSHEET_STORAGE = MyS3BotoStorage(
        acl='public-read',
        bucket=settings.AWS_BUCKET_NAME,
        querystring_auth=True,
    )



class Problem(TranslatableModel):
	slug = models.SlugField() 

	def __unicode__(self):
		return self.translated('name')

class ProblemTranslation(get_translation_model(Problem, "problem")):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name


class Worksheet(TranslatableModel):
	slug = models.SlugField()
	problems = models.ManyToManyField('Problem')

	def related_worksheets(self):
		"Method to pick out related worksheets"
		return Worksheet.objects.filter(problems__in=self.problems.all()).exclude(id=self.id)

from django.utils.text import slugify

def worksheet_file_name(instance, filename):
	return slugify(instance.title) + "." + filename.split(".")[-1]


class WorksheetTranslation(get_translation_model(Worksheet, "worksheet")):
	title = models.CharField(max_length=255)	
	description = models.TextField()
	pdf = models.FileField(upload_to=worksheet_file_name, storage=PSYTOOLS_WORKSHEET_STORAGE, blank=True, null=True)
	tags = models.ManyToManyField('Tag', blank=True)

	def __unicode__(self):
		return self.title