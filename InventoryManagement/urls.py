from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #for the base functionality
    url(r'^$', 'InventoryManagement.views.home', name='home'),
    
    
    #all the urls for the Garments App
    url(r'^Garments/',include('garments.urls')),
    
    #all the urls for the Lighting App
    url(r'^Lighting/',include('lighting.urls')),
    
    #all the urls for the groceries App
    url(r'^Groceries/',include('groceries.urls')),
    
    #all the urls for the drinks App
    url(r'^Drinks/',include('drinks.urls')),
    
    #all the urls for the Admin app
    url(r'^Admin/',include('admin.urls')),
    
    
    
    # url(r'^InventoryManagement/', include('InventoryManagement.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
