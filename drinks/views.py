# Create your views here.
import os
import inspect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from Logging.LogModule import info_flag, PassMessasge, getfileInfo, error_flag
from django.template.context import RequestContext
import datetime
from admin.models import user_business_map,exec_log
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
file_path=os.path.realpath(os.path.abspath(__file__))    
def home(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo,"Redirecting Page",info_flag)
    current_user=user_business_map.objects.filter(category='D').get(user_id=request.user.id)
    if current_user.is_staff:
        return HttpResponseRedirect(reverse('drinks.views.manager_home'))
    else:
        return HttpResponseRedirect(reverse('drinks.views.employee_home'))
    
    
def manager_home(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo,"In Drinks Manager Home Page",info_flag)
    return render_to_response('drinks/manager/Home.html',{})

def employee_home(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo,"In Drinks Employee Home Page",info_flag)
    return render_to_response('drinks/employee/Home.html',{})

def AddUser(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo,"In Drinks Section Add User Page",info_flag)
    return render_to_response('drinks/manager/AddUser.html',{},context_instance=RequestContext(request))

def enlist_new_user(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    if request.method=='POST':
        PassMessasge(sModuleInfo, "Registration for user %s:%s is submitted"%(request.POST['InputFullName'],request.POST['InputUserName']), info_flag)
        current_date_time=datetime.datetime.now()
        temp_user=User()
        temp_user.username=request.POST['InputUserName']
        temp_user.first_name=request.POST['InputFullName']
        temp_user.email=request.POST['InputEmail']
        temp_user.set_password(request.POST['InputPassword'])
        temp_user.date_joined=current_date_time
        temp_user.save()
        PassMessasge(sModuleInfo, "Info for user %s:%s is enlisted in auth_user"%(request.POST['InputFullName'],request.POST['InputUserName']),info_flag)
        #get the current user password
        current_user_id=User.objects.get(first_name__exact=request.POST['InputFullName'],username__exact=request.POST['InputUserName'])
        PassMessasge(sModuleInfo,"Assigning the busniess setting for user %s:%s"%(request.POST['InputFullName'],request.POST['InputUserName']), info_flag)
        business_map=user_business_map()
        business_map.user=current_user_id
        business_map.category=request.POST['InputSection']
        if request.POST['InputRole']=='M':
            business_map.is_staff=True
        if request.POST['InputRole']=='E':
            business_map.is_staff=False
        business_map.save()
        if request.user.is_authenticated():
            execlog=exec_log()
            execlog.user=request.user
            execlog.section=request.POST['InputSection']
            execlog.action="Registered"
            execlog.detail="User %s: Full Name:%s"%(request.POST['InputUserName'],request.POST['InputFullName'])
            execlog.save()
        PassMessasge(sModuleInfo, "Assiging the business setting for user %s:%s"%(request.POST['InputFullName'],request.POST['InputUserName']), info_flag)
        return HttpResponseRedirect(reverse('drinks.views.ListUser'))
    else:
        PassMessasge(sModuleInfo, "Registration for user %s:%s is to be a POST request"%(request.POST['InputFullName'],request.POST['InputUserName']), error_flag)
        return HttpResponseRedirect(reverse('drinks.views.AddUser'))  

def ListUser(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo, "Retrieving all the users", info_flag)
    all_users=user_business_map.objects.filter(category='D').select_related('user_id')
    final_list=[]
    for x in all_users:
        if x.is_staff:
            final_list.append((x.user.first_name,x.user.email,"Manager",x.get_category_display(),x.user.date_joined.date()))
        else:
            final_list.append((x.user.first_name,x.user.email,"Employee",x.get_category_display(),x.user.date_joined.date()))
    #print final_list
    column=['Full Name','Email','Role','Section','Date Registerd']
    return render_to_response('drinks/manager/ListAllUser.html',{'user_list':final_list,'column':column})