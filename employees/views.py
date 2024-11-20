from django.shortcuts import render,redirect
from .models import Employee, PerformanceReview
from .forms import UserForm, EmployeeForm, PerformanceReviewForm

# Create your views here.

def home(request):
    return render(request, 'employees/home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = Employee.objects.get(pk=pk)
    reviews = PerformanceReview.objects.filter(employee=employee)
    return render(request, 'employees/employee_detail.html', {'employee': employee, 'reviews': reviews})

def employee_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        employee_form = EmployeeForm(request.POST, request.FILES)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            employee = employee_form.save(commit=False)
            employee.user = user
            employee.save()
            return redirect('employee_list')
    else:
        user_form = UserForm()
        employee_form = EmployeeForm()
    return render(request, 'employees/employee_form.html', {
        'user_form': user_form,
        'employee_form': employee_form
    })

def employee_edit(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=employee.user)
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            return redirect('employee_list')
    else:
        user_form = UserForm(instance=employee.user)
        employee_form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_form.html', {
        'user_form': user_form,
        'employee_form': employee_form
    })

def employee_delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.user.delete()
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

def review_list(request):
    reviews = PerformanceReview.objects.all()
    return render(request, 'employees/review_list.html', {'reviews': reviews})

def review_create(request):
    if request.method == 'POST':
        form = PerformanceReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = PerformanceReviewForm()
    return render(request, 'employees/review_form.html', {'form': form})

def review_detail(request, pk):
    review = PerformanceReview.objects.get(pk=pk)
    return render(request, 'employees/review_detail.html', {'review': review})
