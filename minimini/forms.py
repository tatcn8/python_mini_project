from django import forms
from .models import Expense, Income

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('cost', 'month', 'id', 'title')

class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = ('title', 'id', 'earner_name', 'value', 'month')