from django.urls import path
from employee.views import employee_add, employee_delete, employee_list, employee_update


urlpatterns = [
    path('', employee_list, name='employee_list'),  # URL for the employee list view
    path('add/', employee_add, name='employee_add'),  # URL for adding a new employee
    path('employee_delete/<int:eid>/', employee_delete, name='employee_delete'),  # URL for deleting an employee by ID
    path('employee_update/<int:eid>/', employee_update, name='employee_update'),  # URL for updating an employee by ID
]