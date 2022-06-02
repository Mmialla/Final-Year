from django.urls import path
from . import views


urlpatterns = [
          path('', views.index, name='homepage'),
          path("login/", views.login, name="login"),
          path("createaccount/", views.createaccount, name="createaccount"),
          path("adminstrator/", views.adminstrator, name="adminstrator"),
          path("adminprofile/", views.adminprofile, name="adminprofile"),
          path("adminuseraccounts/", views.adminuseraccounts, name="adminuseraccounts"),
          path("admincontacts/", views.admincontacts, name="admincontacts"),
          path("bursar/", views.bursar(request), name="admincontacts"),



          path("demo/", views.demo, name="demo"),
          
]