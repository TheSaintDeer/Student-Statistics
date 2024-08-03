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
    fieldsets = (
        ("General", {"fields": ("name", "is_deleted", "arrival")}),
        ("Residence Permit", {"fields": ('submission_of_residence_permit', 'approval_of_residence_permit')}),
        ("Visa", {"fields": ('visa_submission', 'visa_approval')})
    )
    jazzmin_section_order = ("General", "Residence Permit", "Visa")

    list_display = ('name', 'is_deleted', 'arrival',
                    'submission_of_residence_permit', 'approval_of_residence_permit',
                    'visa_submission', 'visa_approval')
    list_editable = ('arrival', 'is_deleted',
                    'submission_of_residence_permit', 'approval_of_residence_permit',
                    'visa_submission', 'visa_approval')
    
    list_filter = ("name",)
    filter_input_length = {
        "name": 3,
    }


admin.site.register(models.Specialization)
admin.site.register(models.CollectingDocumetsStage)
admin.site.register(models.ResidencePermitStage)
admin.site.register(models.AfterMoveStage)