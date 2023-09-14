from django.db import models

# Create your models here.

class Vechile(models.Model):
    vechile_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    seating_capacity = models.IntegerField()
    rent_per_day = models.IntegerField()
    availability = models.BooleanField(default=True)
    vechile_image = models.ImageField(upload_to="vechile_pics")

    def __str__(self):
        return self.vechile_number

