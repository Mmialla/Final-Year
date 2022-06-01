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
          path("login/", views.bursar, name="login"),
          path("contact/", views.bursar, name="contact-page"),
          path("resetPwd/", views.bursar, name="reset-pwd"),
          path("skcontact/", views.bursar, name="projects"),
          path("skdashboard/", views.bursar, name="sk-dashboard"),
          path("skaccounts/", views.bursar, name="sk-accounts"),
          path("useraccounts/", views.bursar, name="user-accounts"),
          path("userprofile/", views.bursar, name="user-profile"),
]