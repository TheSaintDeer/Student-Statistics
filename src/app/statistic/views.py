import datetime

from rest_framework import viewsets, mixins, status
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from core import serializers, models


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    lookup_field = 'name'

    @action(detail=False, methods=['get'])
    def deleted_students(self, request):
        queryset = get_list_or_404(self.get_queryset(), is_deleted=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def filter(self, request: Request):
        params = request.query_params
        if 'start_time' in params:
            queryset = get_list_or_404(models.Student.objects.values('name', 'arrival'), 
                                       arrival__gte=params['start_time'], arrival__lte=params['end_time'])

            data = list()
            for object in queryset:
                data.append({'name': object['name'], 'arrival': object['arrival']})

            return Response(data, status=status.HTTP_200_OK)

        elif 'university' in params:
            queryset = get_list_or_404(models.Specialization.objects.select_related("student").
                                       values('student__name', 'direction', 'specialization').order_by("student__name"), 
                                       university__name=params['university'])
            
            data = list()
            for object in queryset:
                direction = models.Specialization.DIRECTIONS[int(object['direction'])]
                data.append(dict(name=object['student__name'], direction=direction, specialization=object['specialization']))

            return Response(data, status=status.HTTP_200_OK)
        elif 'direction' in params:
            queryset = get_list_or_404(models.Specialization.objects.select_related("student", "university").
                                       values('student__name', 'university__name', 'specialization').order_by("student__name"), 
                                       direction=params['direction'])
            data = list()
            for object in queryset:
                data.append(dict(name=object['student__name'], university=object['university__name'], specialization=object['specialization']))

            return Response(data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = models.University.objects.all()
    serializer_class = serializers.UniversitySerializer
    lookup_field = 'name'


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

    def create(self, request, *args, **kwargs):
        data = {
            'specialization': request.data['specialization'],
            'direction': request.data['direction']
        }

        if request.data['student_name']:
            data['student'] = models.Student.objects.get(name=request.data['student_name']).pk
        else: 
            data['student'] = request.data['student']

        if request.data['university_name']:
            data['university'] = models.University.objects.get(name=request.data['university_name']).pk
        else: 
            data['university'] = request.data['university']

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CollectingDocumetsStageViewSet(viewsets.ModelViewSet):
    queryset = models.CollectingDocumetsStage.objects.all()
    serializer_class = serializers.CollectingDocumetsStageSerializer


class ResidencePermitStageViewSet(viewsets.ModelViewSet):
    queryset = models.ResidencePermitStage.objects.all()
    serializer_class = serializers.ResidencePermitStageSerializer


class AfterMoveStageViewSet(viewsets.ModelViewSet):
    queryset = models.AfterMoveStage.objects.all()
    serializer_class = serializers.AfterMoveStageSerializer