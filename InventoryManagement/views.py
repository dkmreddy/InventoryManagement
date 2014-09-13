'''
Created on Sep 6, 2014

@author: Raju
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext
import inspect
from Logging.LogModule import PassMessasge,getfileInfo,error_flag,info_flag,warning_flag
import os

file_path=os.path.realpath(os.path.abspath(__file__))

def home(request):
    sModuleInfo=getfileInfo(file_path)+inspect.stack()[0][3]
    PassMessasge(sModuleInfo, "In the home page",info_flag)
    return  render_to_response('base/signin.html',{},context_instance=RequestContext(request))

def LoginApprove(request):
    sModuleInfo=getfileInfo(file_path)+ inspect.stack()[0][3]
    print request