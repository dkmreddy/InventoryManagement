'''
Created on Sep 7, 2014

@author: J
'''
from django.conf.urls import patterns, url
urlpatterns = patterns('',
    # Examples:
    url(r'^$','drinks.views.home',name="drinks_home"),
    url(r'^Manager/Home/$', 'drinks.views.manager_home', name='manager_home'),
    url(r'^Manager/AddUser/$','drinks.views.AddUser', name="drinks_add_user"),
    url(r'^Manager/enlist_new_user/$','drinks.views.enlist_new_user', name="drinks_enlist_new_user"),
    url(r'^Manager/ListUser/$','drinks.views.ListUser',name="drinks_list_user"),
    #employee
    url(r'^Employee/Home/$', 'drinks.views.employee_home', name='employee_home'),
)