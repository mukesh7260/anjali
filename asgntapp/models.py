from django.db import models

# Create your models here.
class   Office(models.Model):
   
    employee_code = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    bank_account_number = models.IntegerField()
    working_days = models.IntegerField()
    no_of_leaves = models.IntegerField()
    provident_fund_number =models.IntegerField()
    fixed_annual_ctc = models.IntegerField()
    monthly_ctc = models.IntegerField()
    balance_leaves = models.IntegerField()
    basic = models.IntegerField()
    hra = models.IntegerField()
    tds = models.IntegerField()

    





        


