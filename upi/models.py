from django.db import models

# Create your models here.
class Apple(models.Model):
    name=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    payment_id=models.CharField(max_length=50)
    paid=models.BooleanField(default=False)