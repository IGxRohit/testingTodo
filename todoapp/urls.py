from django.urls import path
from todoapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("savedata",views.savedata),
    path("delete/<int:id>",views.delete),
    path("update/<int:id>",views.update),
    path("updatedata/<int:id>",views.updating),
   

]