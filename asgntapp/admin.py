from django.contrib import admin
from asgntapp.models import Office

# Register your models here.
@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = [ 'id','employee_code', 'employee_name' , 'birth_date', 'designation',
                            'department', 'date_of_joining' ,
                            'bank_account_number', 'working_days','no_of_leaves',
                            'provident_fund_number', 'fixed_annual_ctc', 'monthly_ctc' , 'balance_leaves' , 'basic', 'hra','tds']
                        


