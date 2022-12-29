from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from apps.models import Doctor, Disease, Specialty, Symptom, MainConnection
from apps.serializers import DoctorSerializer, DiseaseSerializer, SpecialitySerializer, SymptomSerializer, \
	MainConnectionSerializer


# Create your views here.
class DoctorViewSet(ModelViewSet):
	queryset = Doctor.objects.all()
	serializer_class = DoctorSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'first_name', 'last_name']


class DiseaseViewSet(ModelViewSet):
	queryset = Disease.objects.all()
	serializer_class = DiseaseSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'title']


class SpecialtyViewSet(ModelViewSet):
	queryset = Specialty.objects.all()
	serializer_class = SpecialitySerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'title']


class SymptomViewSet(ModelViewSet):
	queryset = Symptom.objects.all()
	serializer_class = SymptomSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'title']
	
	def get_object(self):
		queryset = self.filter_queryset(self.get_queryset())
		# make sure to catch 404's below
		obj = queryset.get(pk=self.request.user.organisation_id)
		self.check_object_permissions(self.request, obj)
		return obj


class MainConnectionViewSet(ModelViewSet):
	queryset = MainConnection.objects.all()
	serializer_class = MainConnectionSerializer
	filter_backends = [SearchFilter, DjangoFilterBackend]
	search_fields = ['id', 'diseaseName']
