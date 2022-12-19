from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import Office
from .serializers import OfficeSerializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class OfficeApi(APIView):
    def post(self, request, format=None):
            print(request.data)
            print(type(request.data['employee_code']))
            Basic = 0.25*(request.data['fixed_annual_ctc'])
            HRA = 0.4*Basic
            TDS = 0.1*(request.data['fixed_annual_ctc'])
            obj = Office()
            obj.employee_code =request.data['employee_code']
            obj.employee_name = request.data['employee_name']
            obj.birth_date = request.data['birth_date']
            obj.designation = request.data['designation']
            obj.department = request.data['department']
            obj.date_of_joining = request.data['date_of_joining']
            obj.bank_account_number = request.data['bank_account_number']
            obj.working_days = request.data['working_days']
            obj.no_of_leaves = request.data['no_of_leaves']
            obj.provident_fund_number = request.data['provident_fund_number']
            obj.fixed_annual_ctc = request.data['fixed_annual_ctc']
            obj.monthly_ctc = request.data['monthly_ctc']
            obj.balance_leaves = request.data['balance_leaves']
            obj.basic =  Basic
            obj.hra = HRA
            obj.tds = TDS
            obj.save()
            serializer =OfficeSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Created'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
                stu = Office.objects.get(id=id)
                serializer = OfficeSerializers(stu)
                return Response(serializer.data)
        obj = Office.objects.get(id = pk)
        obj ={
        "name":obj.employee_code,
        "code":obj.employee_name,
        "dob" :obj.birth_date,
        "deg":obj.designation,
        "dept":obj.department,
        "doj":obj.date_of_joining,
        "bacn":obj.bank_account_number,
        "wdays": obj.working_days,
        "leaves":obj.no_of_leaves,
        "pf":obj.provident_fund_number,
        "fctc":obj.fixed_annual_ctc,
        "mctc":obj.monthly_ctc,
        "blcl":obj.balance_leaves
        }
        serializer = OfficeSerializers(obj, many=True)
        return Response(serializer.data)
 
  
  

  
                
          
             
                 
       
