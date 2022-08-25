
from django.db import models

from administrador.models import Usuario

# Create your models here.

class Categoria(models.Model):
    id= models.AutoField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen= models.TextField(default="https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
    # creando la relacion entre el modelo categorias y usuario    
    adminId=models.ForeignKey(to=Usuario,related_name='categorias',db_column='admin_id', on_delete=models.CASCADE)


    class Meta:
        db_table='categorias'
        ordering=['id']

