from django.contrib import admin

from . import models


admin.site.register(models.Student)
admin.site.register(models.University)
admin.site.register(models.Direction)
admin.site.register(models.Specialization)
admin.site.register(models.CollectingDocumetsStage)
admin.site.register(models.UniversityChoiceStage)
admin.site.register(models.ResidencePermitStage)
admin.site.register(models.PreparingToMoveStage)