from django.shortcuts import render_to_response

def manager_home(request):
    return render_to_response('garments/manager/Home.html',{})

def employee_home(request):
    return render_to_response('garments/employee/Home.html',{})