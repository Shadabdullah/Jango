from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("",emp_home),
    path('add/',add_emp),
    path('delete-emp/<int:emp_id>',deleteEmp),
    path('update-emp/<int:emp_id>',updateEmp),
    path('do-update/<int:emp_id>',doUpdate)
]
