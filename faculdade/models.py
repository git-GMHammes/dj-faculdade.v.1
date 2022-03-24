from re import A
from this import d
from django.db import models


class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        txt = "{0}(duracion:{1}año(s))"
        return txt.format(self.nombre, self.duracion)


class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellido = models.CharField(max_length=35)
    nombre = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [('F', 'Femenino'), ('M', 'Masculino')]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    carrera = models.ForeignKey(
        Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0},{1}"
        return txt.format(self.apellido, self.nombre)

    def __str__(self):
        txt = "{0}/carrera: {1})"
        if self.vigencia:
            estadoEstudiante = "vigente"
        else:
            estadoestudiante = "de baja"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)


class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0}({1})/docente:{2}"
        return txt.format(self.nombre, self.codigo, self.docente)


class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(
        Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(
        Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} matriculad{1} en el curso {2}/fecha{3}"
        if self.estudiante.sexo == "F":
            letrasexo = "a"
        else:
            letrasexo = "o"
        fecmat = self.fechaMatricula.strftime(" %A %d/%m/%y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letrasexo,  self.curso, fecmat)
