from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import authentication,permissions
from rest_framework.response import Response
from .serializers import RentSer
from .models import Rent
from vechile.models import Vechile
from datetime import date
from rest_framework.decorators import action
from django.contrib.auth.models import User

# Create your views here.

class RentView(ModelViewSet):
    serializer_class = RentSer
    queryset = Rent.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def calculate_fine(self, borrow_instance):
        current_date=date.today()
        days_overdue = (current_date - borrow_instance.date_of_return).days
        fine_per_day = 50  # Adjust this to your fine policy
        if days_overdue > 0 and borrow_instance.returned is False:
            fine_amount = max(0, days_overdue * fine_per_day)
        else:
            fine_amount=0
        return fine_amount

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Calculate and update the fine for each instance in the queryset
        for instance in queryset:
            instance.fine = self.calculate_fine(instance)
            instance.save()

        ser = self.get_serializer(queryset, many=True)
        return Response(data=ser.data)
    
    @action(methods=['POST'],detail=True)
    def borrow_this_vehicle(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        v=Vechile.objects.get(id=id)
        user=request.user
        ser=RentSer(data=request.data)
        if ser.is_valid():
            v.availability=False
            v.save()
            user.save()
            ser.save(user=user,vec=v)
            return Response(data=ser.data)
        return Response(data=ser.errors)
