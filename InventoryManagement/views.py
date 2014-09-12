'''
Created on Sep 6, 2014

@author: Raju
'''
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def home(request):
    return  render_to_response('base/signin.html',{},context_instance=RequestContext(request))

def LoginApprove(request):
    print request