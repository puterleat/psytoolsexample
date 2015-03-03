from django.contrib import admin
from models import *
from django.conf import settings


class WorksheetTranslationInlineAdmin(admin.StackedInline):
    verbose_name = "Translation"
    verbose_name_plural = "Translations"
    model = WorksheetTranslation
    max_num = len(settings.LANGUAGES)
    extra = 1

class WorksheetAdmin(admin.ModelAdmin):
    inlines = [WorksheetTranslationInlineAdmin,]




class ProblemTranslationInlineAdmin(admin.StackedInline):
    verbose_name = "Translation"
    verbose_name_plural = "Translations"
    model = ProblemTranslation
    max_num = len(settings.LANGUAGES)
    extra = 1

class ProblemAdmin(admin.ModelAdmin):
    inlines = [ProblemTranslationInlineAdmin,]



admin.site.register(Worksheet, WorksheetAdmin)
admin.site.register(Problem, ProblemAdmin)
admin.site.register(Tag)
