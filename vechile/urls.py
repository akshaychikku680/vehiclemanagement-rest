from django.urls import path
from .views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
route = DefaultRouter()

route.register('user',SignUp,basename="signup")
route.register("vechile",VehicleView,basename="vechile")

urlpatterns = [
    path('token',views.obtain_auth_token)
] + route.urls