from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
from .serializers import ActualizarCategoriaSerializer, CategoriaSerializer, CrearCategoriaSerializer, EliminarCategoriaSerializer, PruebaSerializer
from .models import Categoria
from rest_framework import status
# agregado
from rest_framework.permissions import IsAuthenticated

@api_view(http_method_names=['GET','POST','PUT','DELETE'])
def inicio(request:Request):
    print(request.data)
    return Response(data={
        'message':'Endpoint de un decorador'
    })

class PruebaView(ListAPIView):
    # en cualquiera de las clases genericas se necesita declarar los atributos queryset, serializer_class
    queryset=[{
        'nombre':'franco',
        'apellido':'rojas'
    }]
    serializer_class=PruebaSerializer

class CategoriasView(ListAPIView):
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer
    # agreagdo
    permission_classes=[IsAuthenticated]
    def get(self,request):
        categorias=self.get_queryset()
        categoriaSerializada= self.serializer_class(instance=categorias,many=True)
        return Response(data={
            'message':'Las categorias son',
            'content':categoriaSerializada.data
        },status=status.HTTP_200_OK)


class CrearCategoriasView(CreateAPIView):
    queryset=Categoria.objects.all()
    serializer_class=CrearCategoriaSerializer
    def post(self,request:Request):
        body= request.data
        print(request.user.nombre)
        body['adminId']=request.user.id
        instanciaSerializador=self.serializer_class(data=body)
        validacion=instanciaSerializador.is_valid(raise_exception=True)
        if validacion== True:
            instanciaSerializador.save()
            
            return Response(data=instanciaSerializador.data, status=status.HTTP_201_CREATED)

class ActualizarCategoriasView(RetrieveUpdateDestroyAPIView):
    serializer_class=ActualizarCategoriaSerializer
    queryset=Categoria.objects.all()    
     

class EliminarCategoriasView(DestroyAPIView):
    serializer_class=EliminarCategoriaSerializer
    queryset=Categoria.objects.all()    
