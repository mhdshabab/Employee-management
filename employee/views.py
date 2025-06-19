from django.shortcuts import redirect, render

from employee.form import EmployeeForm
from employee.models import EmployeeTable

# Create your views here.
def employee_list(request):
    obj = EmployeeTable.objects.all()  # Fetch all employee records from the database
    return render(request, 'employees/employee_screen.html', {'obj': obj})  # Render the template with the context

def employee_add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Make sure this URL name exists
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def employee_delete(request, eid):
    try:
        employee = EmployeeTable.objects.get(id=eid)  # Fetch the employee by ID
        employee.delete()  # Delete the employee record
    except EmployeeTable.DoesNotExist:
        pass  # Handle the case where the employee does not exist
    return redirect('employee_list')  # Redirect to the employee list view

def employee_update(request, eid):
    try:
        employee = EmployeeTable.objects.get(id=eid)  # Fetch the employee by ID
    except EmployeeTable.DoesNotExist:
        return redirect('employee_list')  # Redirect if the employee does not exist

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  # Redirect to the employee list view
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/update_employee.html', {'obj': employee})  # Render the update form


