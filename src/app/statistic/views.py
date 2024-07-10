from rest_framework import viewsets

from core import serializers, models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = models.Direction.objects.all()
    serializer_class = serializers.DirectionSerializer


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer


class CollectingDocumetsStageViewSet(viewsets.ModelViewSet):
    queryset = models.CollectingDocumetsStage.objects.all()
    serializer_class = serializers.CollectingDocumetsStageSerializer


class UniversityChoiceStageViewSet(viewsets.ModelViewSet):
    queryset = models.UniversityChoiceStage.objects.all()
    serializer_class = serializers.UniversityChoiceStageSerializer


class ResidencePermitStageViewSet(viewsets.ModelViewSet):
    queryset = models.ResidencePermitStage.objects.all()
    serializer_class = serializers.ResidencePermitStageSerializer


class PreparingToMoveStageViewSet(viewsets.ModelViewSet):
    queryset = models.PreparingToMoveStage.objects.all()
    serializer_class = serializers.PreparingToMoveStageSerializer