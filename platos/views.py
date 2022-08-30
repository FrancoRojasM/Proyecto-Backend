from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
from .serializers import ActualizarPlatosSerializer, CrearPlatosSerializer, EliminarPlatosSerializer, PruebaPlatosSerializer,PlatosSerializer
from .models import Platos
from rest_framework import status
# agregado
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(http_method_names=['GET','POST','PUT','DELETE'])
def inicioplatos(request:Request):
    print(request.data)
    return Response(data={
        'message':'Endpoint de un decorador'
    })

class PruebaPlatosView(ListAPIView):
    # en cualquiera de las clases genericas se necesita declarar los atributos queryset, serializer_class
    queryset=[{
        'nombre':'michael',
        'apellido':'chonta'
    }]
    serializer_class=PruebaPlatosSerializer

class PlatosView(ListAPIView):
    queryset=Platos.objects.all()
    serializer_class=PlatosSerializer
    permission_classes=[IsAuthenticated]
    def get(self,request):
        platos=self.get_queryset()        
        platoSerializado= self.serializer_class(instance=platos,many=True)
        return Response(data={
            'message':'Los platos son',
            'content':platoSerializado.data
        },status=status.HTTP_200_OK)

class CrearPlatosView(CreateAPIView):
    queryset=Platos.objects.all()
    serializer_class=CrearPlatosSerializer
    def post(self,request:Request):
        body= request.data
        print(request.user.nombre)
        body['adminId']=request.user.id
        instanciaSerializador=self.serializer_class(data=body)
        validacion=instanciaSerializador.is_valid(raise_exception=True)
        if validacion== True:
            instanciaSerializador.save()
            
            return Response(data=instanciaSerializador.data, status=status.HTTP_201_CREATED)

class ActualizarPlatosView(RetrieveUpdateDestroyAPIView):
    serializer_class=ActualizarPlatosSerializer
    queryset=Platos.objects.all()    

class EliminarPlatosView(DestroyAPIView):
    serializer_class=EliminarPlatosSerializer
    queryset=Platos.objects.all()    