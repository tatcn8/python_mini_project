from django.shortcuts import render, redirect
from .models import Expense, Income
# from rest_framework import generics
# from .serializers import ExpenseSerializer, IncomeSerializer
from django.http import JsonResponse, HttpResponse
from .forms import ExpenseForm, IncomeForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def home_page(request,):
    return render(request, 'minimini/home.html')

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'minimini/expense_list.html', {'expenses': expenses})

@login_required
def expense_detail(request, pk):
    expense = Expense.objects.get(id=pk)
    return render(request, 'minimini/expense_detail.html', {'expense': expense})

# def expense_create(request):
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             expense = form.save()
#             return redirect('expense_detail', pk=expense.pk)
#     else:
#         form = ExpenseForm()
#     return render(request, 'minimini/expense_form.html', {'form': form})

class ExpenseCreate(LoginRequiredMixin, CreateView):
  model = Expense
  fields = ['title', 'cost', 'month']
  
  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)
  

class ExpenseUpdate(LoginRequiredMixin, UpdateView):
  model = Expense
  fields = ['title', 'cost', 'month']
  

class ExpenseDelete(LoginRequiredMixin, DeleteView):
  model = Expense
  success_url = '/expenses/'

@login_required
def expense_edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            expense = form.save()
            return redirect('expense_detail', pk=expense.pk)
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'minimini/expense_form.html', {'form': form})

# @login_required
# def expense_delete(request, pk):
#     Expense.objects.get(id=pk).delete()
#     return redirect('expense_list')
@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'minimini/income_list.html', {'incomes': incomes})
@login_required
def income_detail(request, pk):
    income = Income.objects.get(id=pk)
    return render(request, 'minimini/income_detail.html', {'income': income})

class IncomeCreate(LoginRequiredMixin, CreateView):
  model = Income
  fields = ['title', 'value', 'month', 'earner_name']
  
  # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class IncomeUpdate(LoginRequiredMixin, UpdateView):
  model = Income
  fields = ['title', 'value', 'month', 'earner_name']

class IncomeDelete(LoginRequiredMixin, DeleteView):
  model = Income
  success_url = '/incomes/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
# def income_create(request):
#     if request.method == 'POST':
#         form = IncomeForm(request.POST)
#         if form.is_valid():
#             income = form.save()
#             return redirect('income_detail', pk=income.pk)
#     else:
#         form = IncomeForm()
#     return render(request, 'minimini/income_form.html', {'form': form})

# def income_edit(request, pk):
#     income = Income.objects.get(pk=pk)
#     if request.method == "POST":
#         form = IncomeForm(request.POST, instance=income)
#         if form.is_valid():
#             income = form.save()
#             return redirect('income_detail', pk=income.pk)
#     else:
#         form = IncomeForm(instance=income)
#     return render(request, 'minimini/income_form.html', {'form': form})

# def income_delete(request, pk):
#     Income.objects.get(id=pk).delete()
#     return redirect('income_list')

# class ExpenseList(generics.ListCreateAPIView):
#     queryset=Expense.objects.all()
#     serializer_class=ExpenseSerializer

# class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Expense.objects.all()
#     serializer_class=ExpenseSerializer

# class IncomeList(generics.ListCreateAPIView):
#     queryset=Income.objects.all()
#     serializer_class=IncomeSerializer

# class IncomeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Income.objects.all()
#     serializer_class=IncomeSerializer

# def expense_list(request):
#     expenses = Expense.objects.all().values('cost', 'id', 'month', 'title') # only grab some attributes from our database, else we can't serialize it.
#     expense_list = list(expenses) # convert our artists to a list instead of QuerySet
#     return JsonResponse(expense_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

# def expense_detail(request, pk):
#     expense = Expense.objects.get(id=pk)
#     return HttpResponse(expense)

# def income_list(request):
#     incomes = Income.objects.all().values('earner_name', 'id', 'month', 'title', 'value') # only grab some attributes from our database, else we can't serialize it.
#     income_list = list(incomes) # convert our artists to a list instead of QuerySet
#     return JsonResponse(income_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.

# def income_detail(request, pk):
#     income = Income.objects.get(id=pk)
#     return HttpResponse(income)

# def income_detail(request, pk):
#     # find tutorial by pk (id)
#     try: 
#         income = Income.objects.get(pk=pk) 
#     except Income.DoesNotExist: 
#         return JsonResponse({'message': 'The income does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    

