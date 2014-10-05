'''
Created on Sep 6, 2014

@author: Raju
'''
from django.conf.urls import patterns, url
urlpatterns = patterns('',
    # Examples:
    url(r'^Manager/Home/$', 'garments.views.manager_home', name='manager_home'),
    url(r'^Employee/Home/$', 'garments.views.employee_home', name='employee_home'),
)
