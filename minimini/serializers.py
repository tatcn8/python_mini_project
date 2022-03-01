from rest_framework import serializers
from .models import Expense, Income

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'title', 'cost', 'month']

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id', 'title', 'value', 'month', 'earner_name']