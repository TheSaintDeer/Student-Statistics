from django.db import models


class Student(models.Model):
    '''Model of each individual student'''
    STAGES = {
        1: 'Collecting Documents',
        2: 'University Choice',
        3: 'Residence Permit',
        4: 'Preparing to Move'
    }

    name = models.CharField(
        max_length=255,
    )
    adequacy = models.SmallIntegerField(
        blank=True,
        null=True
    )
    universities = models.ManyToManyField(
        'University',
        blank=True,
        through='Specialization'
    )
    arrival = models.DateField(
        blank=True,
        null=True,
    )
    current_stage = models.CharField(
        max_length=255,
        choices=STAGES,
        default=1
    )

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


class UniversityChoiceStage(Stage):
    '''Model with university selection step'''
    pass


class ResidencePermitStage(Stage):
    '''Model for the stage of collecting documents for applying for a residence permit'''
    pass


class PreparingToMoveStage(Stage):
    '''Abstract model for stages after visa approval'''
    pass