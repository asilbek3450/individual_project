from django.urls import path

from .views import DoctorViewSet, DiseaseViewSet, SpecialtyViewSet, SymptomViewSet, \
	MainConnectionViewSet

urlpatterns = [
	path('doctor/', DoctorViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
	path('disease/', DiseaseViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
	path('speciality/', SpecialtyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
	path('symptom/', SymptomViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
	path('main_connection/', MainConnectionViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
	
]

