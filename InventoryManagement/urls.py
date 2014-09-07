from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'InventoryManagement.views.home', name='home'),
    url(r'^Garments/',include('garments.urls')),
    url(r'^Lighting/',include('lighting.urls')),
    url(r'^Groceries/',include('groceries.urls')),
    url(r'^Drinks/',include('drinks.urls')),
    # url(r'^InventoryManagement/', include('InventoryManagement.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
