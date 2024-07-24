from django.contrib import admin

from . import models


class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name', ]
    filter_input_length = {
        "name": 3,
    }


admin.site.register(models.Student)
admin.site.register(models.University, UniversityAdmin)
admin.site.register(models.Specialization)
admin.site.register(models.CollectingDocumetsStage)
admin.site.register(models.UniversityChoiceStage)
admin.site.register(models.ResidencePermitStage)
admin.site.register(models.PreparingToMoveStage)