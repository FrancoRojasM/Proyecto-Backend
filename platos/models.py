from django.db import models

from administrador.models import Usuario

from categorias.models import Categoria
# Create your models here.

class Platos(models.Model):
    id= models.AutoField(primary_key=True, unique=True)
    nombre= models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen= models.TextField(default="https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")  
    precio=models.DecimalField(max_digits=4,decimal_places=2)
    stock=models.IntegerField()
     # creando la relacion entre el modelo tarea y usuario
    adminId=models.ForeignKey(to=Usuario,related_name='platos',db_column='admin_id', on_delete=models.CASCADE)
    categoriasId=models.ForeignKey(to=Categoria,related_name='platos',db_column='categorias_id',on_delete=models.CASCADE)

    class Meta:
        db_table='platos'
        ordering=['id']
