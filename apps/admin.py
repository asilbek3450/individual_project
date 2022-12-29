from django.contrib import admin

from apps.models import Doctor, Symptom, Specialty, Disease, MainConnection

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(Specialty)
admin.site.register(Symptom)
admin.site.register(MainConnection)
