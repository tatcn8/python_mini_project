from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
# tunr/models.py
class Expense(models.Model):
    title = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('expense_detail', kwargs={'pk': self.id})

class Income(models.Model):
    title = models.CharField(max_length=100)
    earner_name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    month = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('income_detail', kwargs={'pk': self.id})