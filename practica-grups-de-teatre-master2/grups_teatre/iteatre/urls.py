from django.conf.urls import patterns, url
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView, DeleteView

from iteatre import views
from models import Alumnat, Ajuntament, GrupTeatre
from views import *
from form import GrupTeatreForm

from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',

    # List alumnat: iteatre/
    url(r'^$', iteatre,
        name='iteatre'),

    # List alumnat: iteatre/alumnats/
    url(r'^alumnat/$',
        ListView.as_view(
            queryset=Alumnat.objects.all(),
            context_object_name='alumnat',
            template_name='alumnatpage.html'),
        name='alumnae_list'),

    # Dona un alumne: iteatre/alumnats/alumnat/1
    url(r'^alumnat/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Alumnat,
            template_name='alumnaepage.html'),
        name='alumnae_detail'),

    url(r'^alumnat/create/$',
        AlumnatCreate.as_view(),
        name='alumnae_create'),

    url(r'^alumnat/edit/(?P<pk>\d+)/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(model=Alumnat, form_class=AlumnatForm),
        name='alumnae_edit'),

    url(r'^alumnat/delete/(?P<pk>\d+)/$', 
        AlumnatDelete.as_view(), name='alumnae_delete'),

    url(r'^ajuntaments/$',
        ListView.as_view(
            queryset=Ajuntament.objects.all(),
            context_object_name='ajuntaments',
            template_name='ajuntamentspage.html'),
        name='ajuntament_list'),
   
    url(r'^ajuntaments/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Ajuntament,
            template_name='ajuntamentpage.html'),
        name='ajuntament_detail'),

    url(r'^grupsdeteatre/$',
        ListView.as_view(
            queryset=GrupTeatre.objects.all(),
            context_object_name='grupsdeteatre',
            template_name='grupsdeteatrepage.html'),
        name='grupdeteatre_list'),

    # Dona un grup de teatre ex: iteatre/grupsdeteatre/grupdeteatre/1/
    url(r'^grupsdeteatre/(?P<pk>\d+)/$',
        GrupTeatreDetail.as_view(),
        name='grupdeteatre_detail'),

    url(r'^grupsdeteatre/create/$',
        GrupTeatreCreate.as_view(),
        name='grupdeteatre_create'),

    url(r'^grupsdeteatre/edit/(?P<pk>\d+)/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(model=GrupTeatre, form_class=GrupTeatreForm),
        name='grupdeteatre_edit'),

    url(r'^grupsdeteatre/delete/(?P<pk>\d+)/$', 
        GrupTeatreDelete.as_view(), name='grupdeteatre_delete'),

	# crear una qualificacio de un grup de teatre ex: iteatre/grupsdeteatre/1/qualificacions/create/
	url(r'^grupsdeteatre/(?P<pk>\d+)/qualificacions/create/$', 'iteatre.views.qualificacio', name='qualificacio_create'),
)

#RESTful API
urlpatterns += patterns('',
    url(r'^api/ajuntaments/$', APIAjuntamentList.as_view(), name='ajuntament-list'),
    url(r'^api/ajuntaments/(?P<pk>\d+)/$', APIAjuntamentDetail.as_view(), name='ajuntament-detail'),
    url(r'^api/grupteatre/$', login_required(APIGrupTeatreList.as_view()), name='grupteatre-list'),
    url(r'^api/grupteatre/(?P<pk>\d+)/$', APIGrupTeatreDetail.as_view(), name='grupteatre-detail'),
    url(r'^api/alumnat/$', APIAlumnatList.as_view(), name='alumnat-list'),
    url(r'^api/alumnat/(?P<pk>\d+)/$', APIAlumnatDetail.as_view(), name='alumnat-detail'),
    # url(r'^api/grupteatrequalificacions/$', APIGrupTeatreQualificacioList.as_view(), name='grupteatrequalificacio-list'),
    # url(r'^api/grupteatrequalificacions/(?P<pk>\d+)/$', APIGrupTeatreQualificacioDetail.as_view(), name='grupteatrequalificacio-detail'),

)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api' ,'json', 'xml'])


