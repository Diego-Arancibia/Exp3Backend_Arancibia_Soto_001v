from django.urls import path
from .views import home,contacto,galeria,conocenos,intranet,producto,agregar_producto,listar_producto, modificar_producto, eliminar_producto,apiferiados

urlpatterns = [
    path(''          , home    ,name="home"),
    path('contacto/' ,contacto ,name="contacto"),
    path('galeria/'  ,galeria  ,name="galeria"),
    path('conocenos/',conocenos,name="conocenos"),
    path('intranet/' ,intranet ,name="intranet"),
    path('producto/' ,producto ,name="producto"),
    path('agregar-producto/',agregar_producto,name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/',eliminar_producto, name="eliminar_producto"),
    path('apiferiados/',apiferiados,name="apiferiados"),

]