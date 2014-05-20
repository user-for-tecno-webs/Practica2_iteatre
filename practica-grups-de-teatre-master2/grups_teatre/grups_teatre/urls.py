from django.conf.urls import patterns, include, url
from iteatre import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'grups_teatre.views.home', name='home'),
    # url(r'^grups_teatre/', include('grups_teatre.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # Uncomment the next line to enable the admin:
    
    url(r'^iteatre/',include('iteatre.urls',namespace='iteatre')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','django.contrib.auth.views.login'),
    
    url(r'^(\w+)/ajuntaments/$', views.all_ajuntaments_jx_page, name='ajuntamentsjxpage'),
    url(r'^(\w+)/ajuntaments/(\d{1,2})/$', views.one_ajuntament_jx_page, name='ajuntamentjxpage'),

    url(r'^(\w+)/grupsdeteatre/$', views.all_grups_de_teatre_jx_page, name='grupsdeteatrejxpage'),
    url(r'^(\w+)/grupsdeteatre/(\d{1,2})$', views.grup_de_teatre_jx_page, name='grupdeteatrejxpage'),

    url(r'^(\w+)/alumnat/$', views.all_alumnat_jx_page, name='alumnatjxpage'),
    url(r'^(\w+)/alumnat/(\d{1,2})/$', views.alumnae_jx_page, name='alumnaejxpage'),	
)







