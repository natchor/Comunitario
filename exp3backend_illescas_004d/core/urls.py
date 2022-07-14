from django.http import request
from django.urls import path
from .views import form_eliminar_user, form_eliminar_vehiculo, form_modificar_usuario, form_modificar_vehiculo, form_user, form_vehiculo, mostrar,inicio,quienes_somos,galeria_foto,registro,competencias

urlpatterns=[

    
    path('',inicio,name="inicio"),
    path('quienes-somos',quienes_somos,name="quienes-somos"),
    path('galeria-fotografica',galeria_foto,name="galeria-forografica"),
    path('competencias',competencias,name="competencias"),
    path('registro',registro,name="registro"),
    path('mostrar',mostrar, name="mostrar"),
    path('form_vehiculo',form_vehiculo, name="form_vehiculo"),
    path('form_user',form_user, name="form_user"),
    path('form_mod_vehiculo/<id>' , form_modificar_vehiculo ,name="form_mod_vehiculo" ),
    path('form_mod_user/<id>' , form_modificar_usuario ,name="form_mod_user" ),
    path('form_mod_vehiculo/<id>' , form_eliminar_vehiculo ,name="form_mod_vehiculo" ),
    path('form_mod_user/<id>' , form_eliminar_user ,name="form_mod_user" ),
    
    

]