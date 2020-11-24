from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html

# Register your models here.
from.models import Coleccion,Categoria,Pieza,Tipo,Perfil,Rol



class PerfilAdmin(admin.ModelAdmin):
    search_fields = ['documento','sexo']
    list_filter = ['id','user','documento','sexo']
    list_display = ('id','user','documento','sexo','id_rol','telefono','foto')

    #
    def foto(self, obj):
        return format_html('<img width="130" height="100" src={} />', obj.avatar.url)

class PiezaAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_filter = ['id','id_categoria','id_tipo']
    list_display = ('id','id_categoria','id_tipo','descripcion','fotos')
    #
    def fotos(self, obj):
        return format_html('<img width="130" height="100" src={} /> <img width="130" height="100"  src="{}" />', obj.reverso.url, obj.anverso.url)


class ColeccionAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_filter = ['id','fecha_c']
    list_display = ('id','id_user_id','id_pieza_id','fecha_c')    


class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['id','categoria']
    list_filter = ['id','categoria']
    list_display = ('id','categoria')


class TipoaAdmin(admin.ModelAdmin):
    search_fields = ['id','tipo']
    list_filter = ['id','tipo']
    list_display = ('id','tipo')    



class RolaAdmin(admin.ModelAdmin):
    search_fields = ['id','rol']
    list_filter = ['id','rol']
    list_display = ('id','rol')  


admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Pieza,PiezaAdmin)
admin.site.register(Tipo, TipoaAdmin)
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(Rol, RolaAdmin)