from django.db import models
from vechile.models import Vechile
from django.contrib.auth.models import User

# Create your models here.

class Rent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vec = models.ForeignKey(Vechile,on_delete=models.CASCADE)
    date_of_borrow = models.DateField(auto_now_add=True)
    date_of_return = models.DateField()
    fine = models.IntegerField(default=0)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username




    