from django.db import models
from django.conf import settings

class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    registered_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
