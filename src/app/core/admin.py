from django.contrib import admin

from . import models


@admin.register(models.University)
class UniversityAdmin(admin.ModelAdmin):
    resource_class = models.University

    list_display = ('pk', 'name')
    list_filter = ('name', )
    filter_input_length = {
        "name": 3,
    }


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'adequacy', 'arrival', 
                    'current_stage', 'is_deleted')
    
    list_editable = ('adequacy', 'arrival', 'current_stage', 'is_deleted')
    list_filter = ("name",)
    filter_input_length = {
        "name": 3,
    }


admin.site.register(models.Specialization)
admin.site.register(models.CollectingDocumetsStage)
admin.site.register(models.UniversityChoiceStage)
admin.site.register(models.ResidencePermitStage)
admin.site.register(models.PreparingToMoveStage)