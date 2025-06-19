from .models import EmployeeTable
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeTable
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'department']
        