# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from admin.models import user_business_map
from Logging.LogModule import PassMessasge,getfileInfo,error_flag,info_flag,warning_flag
import inspect
import os
import datetime
from django.core.urlresolvers import reverse
file_path=os.path.realpath(os.path.abspath(__file__))

def home(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo,"In Admin Home Page",info_flag)
    return render_to_response('admin/Home.html',{})

def AddUser(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo,"In Add User Page",info_flag)
    return render_to_response('admin/AddUser.html',{},context_instance=RequestContext(request))

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
        if request.POST['InputSection']=='A':
            temp_user.is_staff=True
        temp_user.save()
        PassMessasge(sModuleInfo, "Info for user %s:%s is enlisted in auth_user"%(request.POST['InputFullName'],request.POST['InputUserName']),info_flag)
        #get the current user password
        current_user_id=User.objects.get(first_name__exact=request.POST['InputFullName'],username__exact=request.POST['InputUserName'])
        PassMessasge(sModuleInfo,"Assigning the busniess setting for user %s:%s"%(request.POST['InputFullName'],request.POST['InputUserName']), info_flag)
        business_map=user_business_map()
        business_map.user=current_user_id
        business_map.category=request.POST['InputSection']
        business_map.save()
        PassMessasge(sModuleInfo, "Assiging the business setting for user %s:%s"%(request.POST['InputFullName'],request.POST['InputUserName']), info_flag)
        return HttpResponseRedirect(reverse('admin.views.AddUser'))
    else:
        PassMessasge(sModuleInfo, "Registration for user %s:%s is to be a POST request"%(request.POST['InputFullName'],request.POST['InputUserName']), error_flag)
        return HttpResponseRedirect(reverse('admin.views.AddUser'))  

def ListUser(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo, "Retrieving all the users", info_flag)
    all_users=user_business_map.objects.select_related('user_id')
    final_list=[]
    for x in all_users:
        final_list.append((x.user.first_name,x.user.email,x.get_category_display(),x.user.date_joined.date()))
    #print final_list
    column=['Full Name','Email','Section','Date Registerd']
    return render_to_response('admin/ListAllUser.html',{'user_list':final_list,'column':column})          