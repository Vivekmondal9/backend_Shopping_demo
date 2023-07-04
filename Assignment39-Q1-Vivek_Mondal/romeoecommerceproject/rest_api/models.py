from django.db import models

class Products(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=2000)
    price=models.FloatField()
    image=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    brand=models.CharField(max_length=200)

