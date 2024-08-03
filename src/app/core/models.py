from django.db import models
from django.db.models import signals 
from django.dispatch import receiver


class Student(models.Model):
    '''Model of each individual student'''

    name = models.CharField(
        max_length=255,
    )
    universities = models.ManyToManyField(
        'University',
        blank=True,
        through='Specialization'
    )

    arrival = models.DateField(blank=True, null=True)
    submission_of_residence_permit = models.DateField(blank=True, null=True)
    approval_of_residence_permit = models.DateField(blank=True, null=True)
    visa_submission = models.DateField(blank=True, null=True)
    visa_approval = models.DateField(blank=True, null=True)

    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class University(models.Model):
    '''Model of universities where you can go to study'''
    name = models.CharField(
        max_length=255,
        unique=True
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = 'universities'
        ordering = ['name']


class Specialization(models.Model):
    '''The model shows the student's choice of specialization at a particular university'''
    DIRECTIONS = {
        1: 'Technical',
        2: 'IT',
        3: 'Humanitarian',
        4: 'Creative',
        5: 'Economic',
        6: 'Natural science'
    }

    specialization = models.CharField(
        max_length=255
    )
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE
    )
    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE
    )
    direction = models.CharField(
        max_length=255,
        choices=DIRECTIONS
    )


class Stage(models.Model):
    '''Model for all stages for entering university and moving'''
    student = models.OneToOneField(
        'Student',
        on_delete=models.CASCADE
    )


class CollectingDocumetsStage(Stage):
    '''Model showing the stage of collecting documents for submission to universities'''
    pass


class ResidencePermitStage(Stage):
    '''Model for the stage of collecting documents for applying for a residence permit'''
    pass


class AfterMoveStage(Stage):
    '''Abstract model for stages after visa approval'''
    pass


@receiver(signals.post_save, sender=Student)
def connect_student_and_the_first_stage(sender, instance, **kwargs):
    '''When a student is created, his first stage is created.'''
    
    if kwargs['created']:
        CollectingDocumetsStage.objects.create(student=instance).save()