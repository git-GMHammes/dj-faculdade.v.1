from django.contrib import admin

from academica.models import Carrera, Curso, Estudiante, Matricula

# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Matricula)
