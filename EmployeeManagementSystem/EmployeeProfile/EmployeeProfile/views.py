from django.shortcuts import render
from .models import Employee, Department, Designation, JobDescription, Location

def index(request):
    return render(request, 'EmployeeProfile/index.html')

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'EmployeeProfile/employees.html', {'employees': employees})

def departments(request):
    departments = Department.objects.all()
    return render(request, 'EmployeeProfile/departments.html', {'departments': departments})

def designations(request):
    designations = Designation.objects.all()
    return render(request, 'EmployeeProfile/designations.html', {'designations': designations})

def jobdescriptions(request):
    jobdescriptions = JobDescription.objects.all()
    return render(request, 'EmployeeProfile/jobdescriptions.html', {'jobdescriptions': jobdescriptions})

def locations(request):
    locations = Location.objects.all()
    return render(request, 'EmployeeProfile/locations.html', {'locations': locations})
