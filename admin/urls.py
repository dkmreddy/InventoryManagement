'''
Created on Sep 12, 2014

@author: Raju
'''
from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'admin.views.home', name='home'),
    url(r'^AddUser/$', 'admin.views.AddUser', name='AddUser'),
)
