from . import views;
from django.urls import path;
from django.urls import path, include;


urlpatterns = [
    path("readfile",views.readGivenFile,name="readfile"),
    path("addDataToFile",views.addDataToFile,name="addToFile"),
    path("delete_Localfile",views.delete_Localfile,name="delete_file")
]