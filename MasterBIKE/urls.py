from mysite.urls import path 
from MasterBIKE import views

urlpatterns = [
    path("", views.index, name="index"),
]