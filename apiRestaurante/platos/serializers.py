from rest_framework import serializers
from.models import Platos


class PruebaPlatosSerializer(serializers.Serializer):
    nombre=serializers.CharField(max_length=40)
    apellido=serializers.CharField(max_length=40)

class PlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Platos
        fields='__all__'

class CrearPlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Platos
        fields='__all__'

class ActualizarPlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Platos
        fields='__all__'

        extra_kwargs={
            'id':{
                'read_only':True
            }
        }  

class EliminarPlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Platos
        fields='__all__'

        extra_kwargs={
            'id':{
                'read_only':True
            }
        }  