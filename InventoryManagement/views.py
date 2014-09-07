'''
Created on Sep 6, 2014

@author: Raju
'''
from django.http.response import HttpResponse
def home(request):
    return  HttpResponse("output")