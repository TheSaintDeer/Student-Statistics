from rest_framework import viewsets, mixins, status
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from core import serializers, models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    lookup_field = 'name'


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer
    lookup_field = 'name'


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