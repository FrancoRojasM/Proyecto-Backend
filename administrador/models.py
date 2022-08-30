from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class ManejoUsuario(BaseUserManager):
    # clase para manejar el comportamiento al crear el usuario con el comando
    def create_user(self,email,nombre,apellido,password):
        if not email:        
            raise ValueError('El usuario debe tener un email')
        email=self.normalize_email(email)
        nuevoUsuario=self.model(email=email,nombre=nombre,apellido=apellido)
        # hasheo de contraseña
        nuevoUsuario.set_password(password)

        nuevoUsuario.save()
        return nuevoUsuario
        
        # creacion de un super usuario por consola
    def create_superuser(self,email,nombre,apellido,password):
        nuevoUsuario=self.create_user(email,nombre,apellido,password)
        nuevoUsuario.is_superuser=True
        nuevoUsuario.is_staff=True
        nuevoUsuario.save()

class Usuario(AbstractBaseUser):
    id=models.AutoField(primary_key=True,unique=True)
    nombre=models.CharField(max_length=45)
    apellido=models.CharField(max_length=45)
    email=models.EmailField(unique=True)
    password=models.TextField()

    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)

    objects=ManejoUsuario()

    USERNAME_FIELD='email'

    REQUIRED_FIELDS=['nombre','apellido']

    class Meta:
        db_table='administrador'