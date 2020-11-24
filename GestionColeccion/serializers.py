from rest_framework import serializers
from .models import Coleccion,Categoria,Pieza,Tipo,Perfil,Rol
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields= ['id','username','first_name','last_name','password','email']


class ColeccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coleccion
        fields = ['id','id_user','id_pieza','fecha_c']


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Categoria
        fields = ['id','categoria']


class PiezaSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Pieza
        fields = ['id','descripcion','anverso','reverso','id_categoria','id_tipo']

class TipoSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Tipo
        fields = ['id','tipo']

class PerfilSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Perfil
        fields = ['id','user','documento','sexo','telefono','direccion','avatar','id_rol']

class RolSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Rol
        fields = ['id','rol']