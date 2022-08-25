from django.urls import path
from .views import ActualizarPlatosView, CrearPlatosView, EliminarPlatosView, PlatosView, PruebaPlatosView, inicioplatos

urlpatterns=[    
    path('inicio',inicioplatos),
    path('prueba',PruebaPlatosView.as_view()),
    path('platos',PlatosView.as_view()),
    path('crear-platos',CrearPlatosView.as_view()),
    path('actualizar-platos/<int:pk>',ActualizarPlatosView.as_view()),    
    path('eliminar-platos/<int:pk>',EliminarPlatosView.as_view())
]