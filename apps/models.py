from django.db import models


# Create your models here.
class Specialty(models.Model):
	title = models.CharField(max_length=100)
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return self.title


class Doctor(models.Model):
	firs_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	specialty_id = models.ForeignKey(Specialty, on_delete=models.CASCADE)
	room_number = models.IntegerField()
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return self.firs_name + ' ' + self.last_name


class Disease(models.Model):
	title = models.CharField(max_length=100)
	speciality_id = models.ForeignKey(Specialty, on_delete=models.CASCADE)
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return self.title


class Symptom(models.Model):
	title = models.CharField(max_length=100, unique=True)
	disease_id = models.ForeignKey(Disease, on_delete=models.CASCADE)
	
	class Meta:
		ordering = ['-id']
	
	def __str__(self):
		return f'{self.id} - {self.title} - disease_id={self.disease_id.id}'


class MainConnection(models.Model):
	diseaseName = models.ForeignKey(Disease, on_delete=models.CASCADE)
	description = models.TextField()
	symptomList = models.ManyToManyField(Symptom)
	
	class Meta:
		ordering = ['id']
	
	def __str__(self):
		return str(self.id) + ' - ' + self.diseaseName.title
	