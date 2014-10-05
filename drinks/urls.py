'''
Created on Sep 7, 2014

@author: J
'''
from django.conf.urls import patterns, url
urlpatterns = patterns('',
    # Examples:
    url(r'^Manager/Home/$', 'drinks.views.manager_home', name='manager_home'),
    url(r'^Employee/Home/$', 'drinks.views.employee_home', name='employee_home'),
)