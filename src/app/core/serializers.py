from rest_framework import serializers

from . import models


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.University
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Direction
        fields = '__all__'


class SpecializationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Specialization
        fields = '__all__'
        

class CollectingDocumetsStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CollectingDocumetsStage
        fields = '__all__'


class UniversityChoiceStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UniversityChoiceStage
        fields = '__all__'


class ResidencePermitStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResidencePermitStage
        fields = '__all__'


class PreparingToMoveStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PreparingToMoveStage
        fields = '__all__'