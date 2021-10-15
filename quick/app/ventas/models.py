from django.db import models

# Create your models here.

class Clients(models.Model):
    document = models.CharField(max_length=20, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.document

    class Meta:
        db_table = 'clients'


class Bills(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    nit = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'bills'

class Products(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bills_products = models.ManyToManyField(Bills, through='BillsProducts')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'

class BillsProducts(models.Model):
    bills = models.ForeignKey(Bills, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        db_table = 'billsproducts'