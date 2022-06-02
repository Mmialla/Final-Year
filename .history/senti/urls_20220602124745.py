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
          path("bursar/", views.bursar, name="bursar"),
          path("bursaraccounts/", views.bursaraccounts, name="bursaraccounts"),
          path("bursarcontacts/", views.bursarcontacts, name="bursarcontacts"),
          path("bursarprofile/", views.bursarprofile, name="bursarprofile"),
          path("shopkeeper/", views.shopkeeper, name="shopkeeper"),
          path("shopkeeperaccounts/", views.shopkeeperaccounts, name="shopkeeperaccounts"),
          path("shopkeeperprofile/", views.shopkeeperprofile(request), name="shopkeeperusers"),
          path("shopkeepercontacts/", views.shopkeepercontacts, name="shopkeepercontacts"),
          
]