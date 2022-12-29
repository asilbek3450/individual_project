from rest_framework.serializers import ModelSerializer

from apps.models import Doctor, Disease, Specialty, Symptom, MainConnection


class DoctorSerializer(ModelSerializer):
	class Meta:
		model = Doctor
		fields = '__all__'
		
		read_only_fields = ['id']
		
		depth = 1


class SpecialitySerializer(ModelSerializer):
	class Meta:
		model = Specialty
		fields = '__all__'
		
		read_only_fields = ['id']
		
		depth = 1


class SymptomSerializer(ModelSerializer):
	class Meta:
		model = Symptom
		fields = '__all__'
		
		read_only_fields = ['id']
		
		depth = 1


class DiseaseSerializer(ModelSerializer):
	class Meta:
		model = Disease
		fields = '__all__'
		
		read_only_fields = ['id']
		
		depth = 1


class MainConnectionSerializer(ModelSerializer):
	class Meta:
		model = MainConnection
		fields = '__all__'
		
		read_only_fields = ['id']
		
		depth = 1
	
	def to_representation(self, instance):
		representation = super().to_representation(instance)
		representation['diseaseName'] = instance.diseaseName.title
		return representation
	