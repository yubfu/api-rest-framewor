from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from .models import Coleccion,Categoria,Pieza,Tipo,Perfil,Rol
from rest_framework import viewsets
from .serializers import ColeccionSerializer, CategoriaSerializer, PiezaSerializer, TipoSerializer, PerfilSerializer, RolSerializer,UserSerializer

# Create your views here.
# Controllers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ColeccionViewSet(viewsets.ModelViewSet):
    queryset = Coleccion.objects.all()
    serializer_class = ColeccionSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class PiezaViewSet(viewsets.ModelViewSet):
    queryset = Pieza.objects.all()
    serializer_class = PiezaSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
   