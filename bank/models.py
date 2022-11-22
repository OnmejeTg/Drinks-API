from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField( max_length=50, blank=True)

def __str__(self):
    return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, blank=True)

def __str__(self):
    return self.name

class Transactions(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='transctions')
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='transaction')

def __str__(self):
    return f'{self.amount} {self.currency} {self.date}'