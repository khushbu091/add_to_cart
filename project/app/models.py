from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=100)
    Descri=models.CharField(max_length=500)
    Image=models.ImageField(upload_to='images/')
    Price=models.IntegerField()
    Quantity=models.IntegerField()