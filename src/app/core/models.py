from django.db import models


class Student(models.Model):
    '''Model of each individual student'''
    name = models.CharField(
        max_length=255
    )
    adequacy = models.SmallIntegerField()
    universities = models.ManyToManyField(
        'University',
        blank=True,
        through='Specialization'
    )
    arrival = models.DateField()
    current_stage = models.ForeignKey(
        'Stage',
        on_delete=models.CASCADE
    )


class University(models.Model):
    '''Model of universities where you can go to study'''
    name = models.CharField(
        max_length=255
    )
    directions = models.ManyToManyField(
        'Direction',
        blank=True,
    )

    class Meta:
        verbose_name_plural = 'Universities'


class Direction(models.Model):
    '''Model indicating directions in universities'''
    name = models.CharField(
        max_length=255
    )


class Specialization(models.Model):
    '''The model shows the student's choice of specialization at a particular university'''
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE
    )
    university = models.ForeignKey(
        'University',
        on_delete=models.CASCADE
    )
    direction = models.ForeignKey(
        'Direction',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255
    )


class Stage(models.Model):
    '''Abstract model for all stages for entering university and moving'''
    pass


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