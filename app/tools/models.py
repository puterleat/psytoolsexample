from django.db import models
from translatable.models import TranslatableModel, get_translation_model

# Create your models here.



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


class WorksheetTranslation(get_translation_model(Worksheet, "worksheet")):
	title = models.CharField(max_length=255)	
	description = models.TextField()
	pdf = models.FileField(upload_to="uploads", blank=True, null=True)
	tags = models.ManyToManyField('Tag', blank=True)

	def __unicode__(self):
		return self.title