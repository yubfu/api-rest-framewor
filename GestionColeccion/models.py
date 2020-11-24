from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

ROL = (
    ("C","Coleccionista"),
    ("V","Vendedor"),
    ("M","ColeccionistaVendedor")
)

class Rol(models.Model):
    rol = models.CharField( max_length=1, choices=ROL , default='C')

    def __str__(self):
        return self.rol

    class Meta:
        verbose_name_plural= _('Rol')


Sexo = (
    ("M","Masculino"),
    ("F","Femenino"),
    ("O","Otro"),
    ("N","No definir")
)

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    documento = models.CharField(max_length= 102, unique=True)
    sexo = models.CharField(max_length=1, choices=Sexo, default='N' )
    telefono= models.CharField(max_length=30, blank=False)
    direccion=models.CharField(max_length=50, blank=False)
    avatar= models.ImageField(verbose_name="Imagen", upload_to="media/profile")
    id_rol=models.ForeignKey(Rol, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return self.user.first_name
     
    class Meta:
        verbose_name_plural= _('Perfil') 

class Categoria(models.Model):
    categoria= models.CharField(max_length=100, blank=False)
     
    def __str__(self):
        return self.categoria 

    class Meta:
        verbose_name_plural= _('Categoria') 

TIPO = (
    ("C","Coleccion"),
    ("V","Venta"), 
)


class Tipo (models.Model):
    tipo = models.CharField(max_length=1, choices=TIPO, default='C' )
    
    def __str__(self):
        return self.tipo 
    class Meta:
        verbose_name_plural= _('Tipo') 

class Pieza(models.Model):
    descripcion=models.TextField(blank=False)
    anverso= models.ImageField(verbose_name="Imagen", upload_to="media/coleccion")
    reverso= models.ImageField(verbose_name="Imagen", upload_to="media/coleccion")
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id) 
    class Meta:
        verbose_name_plural= _('Pieza') 


class Coleccion(models.Model):
    id_user = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    id_pieza = models.ForeignKey(Pieza, on_delete=models.CASCADE)
    fecha_c = models.DateTimeField()

    def __str__(self):
        return str({self.id_user_id, self.id_pieza_id, self.fecha_c})
    class Meta:
        verbose_name_plural= _('Colección') 

