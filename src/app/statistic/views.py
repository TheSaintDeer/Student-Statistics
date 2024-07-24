from rest_framework import viewsets, mixins, status
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import action
from rest_framework.response import Response

from core import serializers, models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def update_by_name(self, request, *args, **kwargs):
        print(request.data)
        student = get_object_or_404(self.get_queryset(), name=request.data['stud_name'])
        serializer = self.get_serializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class UniversityViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer

    @action(detail=False, methods=['delete'])
    def destroy_by_name(self, request):
        university = get_object_or_404(self.get_queryset(), name=request.data['name'])
        self.perform_destroy(university)
        return Response(status=status.HTTP_204_NO_CONTENT)

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