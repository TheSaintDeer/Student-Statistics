from django.urls import path, include
from rest_framework import routers

from . import views


app_name = 'statistic'

router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)
router.register(r'university', views.UniversityViewSet)
router.register(r'specialization', views.SpecializationViewSet)
router.register(r'collecting-documets', views.CollectingDocumetsStageViewSet)
router.register(r'university-choice', views.UniversityChoiceStageViewSet)
router.register(r'residence-permit', views.ResidencePermitStageViewSet)
router.register(r'preparing-to-move', views.PreparingToMoveStageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]