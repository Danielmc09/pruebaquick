from django.db import models
from app.clients.models import Clients
from app.products.models import Products
# Create your models here.

class Bills(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    bills_products = models.ManyToManyField(Products, related_name='content')

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'bills'