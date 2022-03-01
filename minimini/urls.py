from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.home_page, name ='homepage'),
    path('expenses/', views.expense_list, name ='expense_list'),
    path('expenses/<int:pk>/', views.expense_detail, name ='expense_detail'),
    path('expenses/create/', views.ExpenseCreate.as_view(), name='expense_create'),
    path('expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expense_edit'),
    path('expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expense_delete'),
    path('incomes/', views.income_list, name ='income_list'),
    path('incomes/<int:pk>/', views.income_detail, name ='income_detail'),
    path('incomes/create/', views.IncomeCreate.as_view(), name='income_create'),
    path('incomes/<int:pk>/update/', views.IncomeUpdate.as_view(), name='income_edit'),
    path('incomes/<int:pk>/delete/', views.IncomeDelete.as_view(), name='income_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]