# Create your views here.

from django.http.response import HttpResponse
from django.shortcuts import render_to_response

def manager_home(request):
    return render_to_response('drinks/manager/Home.html',{})

def employee_home(request):
    return render_to_response('drinks/employee/Home.html',{})