from django.db import models

# Create your models here.
from django.db import models

class UmraTour(models.Model):
    airline = models.CharField(max_length=100)
    duration_days = models.IntegerField()
    meals_per_day = models.IntegerField()
    visa_included = models.BooleanField(default=False)
    medical_assistance = models.BooleanField(default=False)
    experienced_guide = models.CharField(max_length=100)
    zamzam_water_liters = models.IntegerField()
    includes_razor = models.BooleanField(default=False)
    includes_bag = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.airline} - {self.duration_days} days"

