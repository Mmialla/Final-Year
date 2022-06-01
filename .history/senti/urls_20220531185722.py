from django.urls import path
from . import views


urlpatterns = [
          path('', views.index, name='homepage'),
          path("admin-bursar/", views.bursar, name="bursar-dashboard"),
          path("admin-pages-contact/", views.bursar, name="admin-contacts"),
          path("admin-user-accounts/", views.bursar, name="admin-accounts"),
          path("userprofiles/", views.bursar, name="user-profiles"),
          path("admin/", views.bursar, name="admin"),
          path("bursar/", views.bursar, name="bursar"),
          path("login/", views.login, name="login"),
          
]