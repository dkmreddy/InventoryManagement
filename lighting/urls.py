'''
Created on Sep 7, 2014

@author: Raju
'''
from django.conf.urls import patterns, url
urlpatterns = patterns('',
    # Examples:
    url(r'^Manager/Home/$', 'lighting.views.manager_home', name='manager_home'),
    url(r'^Employee/Home/$', 'lighting.views.employee_home', name='employee_home'),
)

