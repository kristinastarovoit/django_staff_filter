from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date

def employee_overview(request):
    all_employees = Employee.objects.all()
    salary_gt_3000 = Employee.objects.filter(salary__gt=3000)
    count_gte_5000 = Employee.objects.filter(salary__gte=5000).count()
    sales_employees = Employee.objects.filter(department__name="Sales")
    sales_average_salary = sales_employees.aggregate(Avg("salary", default=0))
    not_hr = Employee.objects.exclude(department__name="HR")
    new_not_hr = not_hr.filter(hire_date__lt=date(2022,1,1))
    # Alternativ:
    # new_not_hr = Employee.objects.exclude(Q(hire_date__gt=date(2022,1,1)) | Q(department__name="HR"))


    context = {
        'all': all_employees,
        'gt_3000': salary_gt_3000,
        'gte_5000': count_gte_5000,
        'avg_sales': sales_average_salary,
        'sales_employees': sales_employees,
        'new_not_hr': new_not_hr
        }
    return render(request, 'employee_list.html', context)
