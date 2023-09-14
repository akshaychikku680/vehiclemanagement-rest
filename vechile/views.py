from django.shortcuts import render
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import authentication,permissions

# Create your views here.

class SignUp(ViewSet):
    def create(self,request,*args,**kwargs):
        ser = SignUpSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"User Created"})
        return Response(data=ser.errors)
    

class VehicleView(ModelViewSet):
    serializer_class = VechileSerializer
    queryset = Vechile.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Vechile.objects.filter(id=id).delete()
        return Response({"msg":"Deleted"})
    
    
   