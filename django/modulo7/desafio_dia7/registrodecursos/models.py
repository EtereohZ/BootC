from django.db import models

# Create your models here.
class Curso (models.Model):
    codigo = models.CharField(max_length=10, primary_key=True)
    nombre =models.CharField(max_length=50, null=False)
    version = models.IntegerField()

    def __str__(self) -> str:
        return f"-{self.codigo} {self.nombre}, {self.version}"
    
class Profesor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    cursos = models.ManyToManyField(Curso, related_name='profesores')
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self) -> str:
        return 

class Estudiante(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField()
    cursos = models.ManyToManyField(Curso, related_name='estudiantes')
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.rut}, {self.nombre} {self.apellido}"


    
class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    dpto = models.CharField(max_length=10, null=True)
    comuna = models.CharField(max_length=20, null=False)
    ciudad = models.CharField(max_length=20, null=False)
    region = models.CharField(max_length=20, null=False)
    estudiante = models.OneToOneField(Estudiante, related_name="direccion", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.calle} #{self.numero} {self.ciudad}, {self.region}"