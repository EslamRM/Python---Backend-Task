from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    category = models.CharField(max_length=200,db_index=True)
    name = models.CharField(max_length=300,db_index=True)
    image = models.URLField()
    brand = models.CharField(max_length=200,db_index=True)
    price = models.DecimalField(default=0,db_index=True,decimal_places=3,max_digits=10)
    quantity = models.IntegerField(default=1,db_index=True)
    rating = models.FloatField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (["name"])
        
    def __str__(self) -> str:
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=300,db_index=True)
    image = models.URLField()
    brand = models.CharField(max_length=200,db_index=True)
    price = models.DecimalField(default=0,db_index=True,decimal_places=3,max_digits=10)
    quantity = models.IntegerField(default=1,db_index=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = (["-added"])
    
    def __str__(self) -> str:
        return self.name