from django.urls import path
from . import views


urlpatterns = [
          path('', views.index, name='homepage'),
          path("login/", views.login, name="login"),
          path("login/", views.login, name="createA"),

]