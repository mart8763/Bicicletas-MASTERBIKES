from mysite.urls import path 
from MasterBIKE import views

urlpatterns = [
    path("", views.index, name="index"),
    path("productos", views.productos, name="productos"),
    path("categoria", views.categoria, name="categoria"),
    path("carro", views.carro, name="carro"),
    path("registro", views.registro, name="registro"),
    path("iniciar_sesion", views.iniciar_sesion, name="iniciar_sesion"),
    path("termino_y_condiciones", views.termino_y_condiciones, name="termino_y_condiciones"),
    path("electrica", views.electrica, name="electrica"),
    path("mtb", views.mtb, name="mtb"),
    path("nino", views.nino, name="nino"),
    path("ruta", views.ruta, name="ruta"),
    path("urbex", views.urbex, name="urbex"),
]