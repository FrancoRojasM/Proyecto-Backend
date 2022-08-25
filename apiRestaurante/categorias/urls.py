from django.urls import path
from .views import ActualizarCategoriasView, CategoriasView, CrearCategoriasView, EliminarCategoriasView, PruebaView, inicio

# rutas
urlpatterns=[
    path('inicio',inicio),
    path('prueba',PruebaView.as_view()),
    path('categorias',CategoriasView.as_view()),
    path('crear-categorias',CrearCategoriasView.as_view()),
    path('actualizar-categorias/<int:pk>',ActualizarCategoriasView.as_view()),
    path('eliminar-categorias/<int:pk>',EliminarCategoriasView.as_view())
]