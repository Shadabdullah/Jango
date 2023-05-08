from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .views import *
from django.http import HttpRequest , request , HttpResponse
from .models import *

# Create your views here.
def emp_home(request):
    emp = Emp.objects.all()
    
    return render(request ,'emp/home.html',{"emp" : emp})

def add_emp(request):
    if request.method=="POST":
        emp_name=request.POST.get("emp_name")
        emp_id=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")

        #validate

        #create model object and set the data
        e=Emp()
        e.name=emp_name
        e.emp_id=emp_id
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True
        #save the object
        e.save()
        return redirect("/Empl/")
  
    
    return render(request, 'emp/add_emp.html',{})

def deleteEmp(request ,emp_id):

    dele = Emp.objects.get(pk=emp_id)
    dele.delete()

    return redirect("/Empl/")

def updateEmp(request ,emp_id):
    emp = Emp.objects.get(pk=emp_id)
    print(emp.department)
    return render(request, 'emp/update_emp.html',{"emp" : emp})


def doUpdate(request,emp_id):
    if request.method=='POST':
        emp_name=request.POST.get("emp_name")
        emp_id_temp=request.POST.get("emp_id")
        emp_phone=request.POST.get("emp_phone")
        emp_address=request.POST.get("emp_address")
        emp_working=request.POST.get("emp_working")
        emp_department=request.POST.get("emp_department")  
    
        e=Emp.objects.get(pk=emp_id)
        e.name=emp_name
        e.emp_id=emp_id_temp
        e.phone=emp_phone
        e.address=emp_address
        e.department=emp_department
        if emp_working is None:
            e.working=False
        else:
            e.working=True

        e.save()
    return redirect("/Empl/")
   