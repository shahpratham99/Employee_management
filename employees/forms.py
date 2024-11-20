from django import forms
from django.contrib.auth.models import User
from .models import Employee, PerformanceReview

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['department', 'position', 'hire_date', 'salary', 'profile_picture', 'bio']

class PerformanceReviewForm(forms.ModelForm):
    class Meta:
        model = PerformanceReview
        fields = ['employee', 'review_date', 'score', 'feedback']
