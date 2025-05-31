from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

def dashboard(request):
    return render(request, 'dashboard.html')

def insert_employee(request):
    if request.method == 'POST':
        try:
            emp = Employee(
                emp_number = request.POST.get('emp_number'),
                emp_name = request.POST.get('emp_name'),
                gender = request.POST.get('gender'),
                birth_date = request.POST.get('birth_date'),
                joining_date = request.POST.get('joining_date'),
                department = request.POST.get('department')
            )
            emp.save()
            return render(request, 'success.html', {'message' : 'Employee inserted successfully!' })
        except Exception as e:
            return render(request, 'success.html', {'message': str(e)})
    else:
        return render(request, 'insert_employee.html')

def update_employee(request):
    if request.method == 'POST':
        emp_number = request.POST.get('emp_number')
        try:
            emp = Employee.objects.get(emp_number=emp_number)
            emp.emp_name = request.POST.get('emp_name')
            emp.gender = request.POST.get('gender')
            emp.birth_date = request.POST.get('birth_date')
            emp.joining_date = request.POST.get('joining_date')
            emp.department = request.POST.get('department')
            emp.save()
            return render(request, 'success.html', {'message': 'Employee updated successfully!'})
        except Exception as e:
            return render(request, 'success.html', {'message' : str(e)})
    return render(request, 'update_employee.html')


def delete_employee(request):
    if request.method == 'POST':
        emp_number = request.POST.get('emp_number')
        try:
            emp = Employee.objects.get(emp_number=emp_number)
            emp.delete()
            return render(request, 'success.html', {'message': 'Employee deleted successfully!'})
        except Exception as e:
            return render(request, 'success.html', {'message' : str(e)})
    return render(request, 'delete_employee.html')

def search_employee(request):
    if request.method == 'POST':
        emp_number = request.POST.get('emp_number')
        try:
            emp = Employee.objects.get(emp_number=emp_number)
            return render(request, 'search_result.html', {'employee' : emp})
        except Employee.DoesNotExist:
            return render(request, 'success.html', {'message': 'Employee not found!'})
        except Exception as e:
            return render(request, 'success.html', {'message' : str(e)})
    return render(request, 'search_employee.html')
