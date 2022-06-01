from django.urls import path
from . import views


urlpatterns = [
          path('', views.index, name='homepage'),
          path("login/", views.login, name="login"),
          path("createaccount/", views.createaccount, name="createaccount"),
          path("adminstrator/", views.adminstrator, name="adminstrator"),
          path("demo/", views.adminstrator, name="adminstrator"),

]