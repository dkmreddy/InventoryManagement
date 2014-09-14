'''
Created on Sep 6, 2014

@author: Raju
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import inspect
from Logging.LogModule import PassMessasge,getfileInfo,error_flag,info_flag,warning_flag
import os
from django.contrib.auth import authenticate,login
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

file_path=os.path.realpath(os.path.abspath(__file__))

def home(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo, "In the Login page",info_flag)
    return  render_to_response('base/signin.html',{},context_instance=RequestContext(request))

def LoginApprove(request):
    sModuleInfo=getfileInfo(file_path)+ inspect.stack()[0][3]
    try:
        if request.method=="POST":
            user_name=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=user_name,password=password)
            if user is not None:
                login(request,user)
                print user
                return HttpResponseRedirect(reverse('admin.views.home'))
            else:
                PassMessasge(sModuleInfo, "(%s,%s)No Such User exists"%(user_name,password),error_flag)
                return HttpResponseRedirect(reverse('InventoryManagement.views.home'))
    except Exception,e:
        PassMessasge(sModuleInfo, str(e),error_flag)
        return HttpResponseRedirect(reverse('InventoryManagement.views.home'))