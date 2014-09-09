'''
Created on Sep 6, 2014

@author: Raju
'''
from django.http.response import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return  render_to_response('base/signin.html')