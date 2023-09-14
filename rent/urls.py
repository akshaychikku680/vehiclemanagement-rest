from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

route = DefaultRouter()

route.register("rent",RentView,basename="rent")

urlpatterns = [
    path('token',views.obtain_auth_token)
] + route.urls