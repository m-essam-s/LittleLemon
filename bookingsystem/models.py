from django.db import models
from django.utils.timezone import now

class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_date = models.DateField(default=now)
    reservation_slot = models.IntegerField()
    name = models.CharField(max_length=255, default="Unnamed Booking")
    phone = models.CharField(max_length=20, default="000-000-0000")  # Default value to avoid migration prompt
    email = models.EmailField(null=True, blank=True)
    guests = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.reservation_date} {self.reservation_slot}"
