# Create your views here.
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import loader, Context, Template
from iteatre.models import *
from django.utils import simplejson
from django.shortcuts import render_to_response
import json
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from form import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from serializers import AjuntamentSerializer, GrupTeatreSerializer, AlumnatSerializer
from rest_framework import generics, permissions

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
    	return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class AlumnatCreate(LoginRequiredMixin,CreateView):
	model = Alumnat
	template_name = 'form.html'
	form_class = AlumnatForm
	
	def from_valid(self, form):
		form.instance.user = self.request.user
		return super(AlumnatCreate, self).form_valid(form)

class GrupTeatreCreate(LoginRequiredMixin,CreateView):
	model = GrupTeatre
	template_name = 'form.html'
	form_class = GrupTeatreForm

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(GrupTeatreCreate, self).form_valid(form)

class LoginRequiredCheckIsOwnerUpdateView(CheckIsOwnerMixin, LoginRequiredMixin, UpdateView):
	template_name='form.html'

class GrupTeatreDelete(DeleteView):
	model = GrupTeatre
	success_url = reverse_lazy('iteatre:grupdeteatre_list')

class AlumnatDelete(DeleteView):
	model = Alumnat
	success_url = reverse_lazy('iteatre:alumnae_list')

def iteatre(request):
	template = get_template('iteatre.html')
	variables = Context({
		'titlehead': 'Gestio de teatres aPP',
		'pagetitle': 'Benvingut/benvinguda a applicio de gestio de grups de teatre',
		'contentbody': 'Managing non legal funding since 2013',
		'user': request.user
		})
	output = template.render(variables)
	return HttpResponse(output)

''' mostrar un ajuntament concret i llistar tots els seus camps en format json/xml '''
def one_ajuntament_jx_page(request, tipus, idAjuntament):
	try:
		a = Ajuntament.objects.get(id = int(idAjuntament))
		if tipus=='json':
			list_ajuntaments = []
			ajuntament= {"id": a.id, "nom": a.nom,
							"telefon":a.telefon, "email":a.email,
							"adreca":a.adreca, "cif":a.cif}
			list_ajuntaments.append(ajuntament)
			ajuntament_json = {"Ajuntament":list_ajuntaments}
			return HttpResponse(json.dumps(ajuntament_json))
		elif tipus=='xml':
			variables = Context({
						'ajuntament': a
						})
			t = loader.get_template('ajuntamentpage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")	
	except:
		raise Http404('Error al generar la pagina')


''' mostrar tots els ajuntaments en format json/xml '''
def all_ajuntaments_jx_page(request, tipus):
	try:
		ajuntaments = Ajuntament.objects.all()
		if tipus=='json':
			list_ajuntaments = []
			for a in ajuntaments:
				ajuntament = {"id": a.id, "nom": a.nom,
								"telefon":a.telefon, "email":a.email,
								"adreca":a.adreca, "cif":a.cif}
				list_ajuntaments.append(ajuntament)
			ajuntaments = {"Ajuntaments": list_ajuntaments}
			return HttpResponse(json.dumps(ajuntaments))
		elif tipus=='xml':
			variables = Context({
						'ajuntaments': ajuntaments
						})
			t = loader.get_template('ajuntamentspage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")
	except:
		raise Http404('Error al generar la pagina')

	
''' mostrar tots els grup de teatre i llistar tots els seus camps en format json/xml '''
def all_grups_de_teatre_jx_page(request, tipus):
	try:
		grups_teatre = GrupTeatre.objects.all()
		if tipus=='json':			
			list_grups = []
			for grup in grups_teatre:
				grup_teatre = {"id": grup.id, "nom": grup.nom,
								"dies_i_horaris":grup.dies_i_horaris}
				list_grups.append(grup_teatre)
			grups_teatre_json = {"Grups Teatre": list_grups}
			return HttpResponse(json.dumps(grups_teatre_json))
		elif tipus=='xml':
			variables = Context({
						'grups': grups_teatre
						})
			t = loader.get_template('grupspage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")	
	except:
		raise Http404('Error al generar la pagina')

	
''' mostrar un grup de teatre concret i llistar tots els camps de teatre en format json/xml '''
def grup_de_teatre_jx_page(request, tipus, idGrupTeatre):
	try:
		grup = GrupTeatre.objects.get(id = int(idGrupTeatre))
		if tipus=='json':			
			list_grups = []
			grup_teatre = {"id": grup.id, "nom": grup.nom,
							"dies_i_horaris":grup.dies_i_horaris,
							}
			list_grups.append(grup_teatre)
			grup_teatre_json = {"Grup de Teatre": list_grups}
			return HttpResponse(json.dumps(grup_teatre_json))
		elif tipus=='xml':
			variables = Context({
						'grup': grup
						})
			t = loader.get_template('gruppage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")
	except:
		raise Http404('Error al generar la pagina')

	
''' mostrar tots els alumnes i els seus camps en format json/xml'''
def all_alumnat_jx_page(request, tipus):
	try:
		alumnat = Alumnat.objects.all()
		if tipus=='json':			
			list_alumnat = []
			for al in alumnat:
				alumnae = {"nom": al.nom, "Tel. personal": al.telefon_personal, 
						"Tel. personal_encarregada":al.telefon_persona_encarregada, 
						"email": al.email, "nif_nie": al.nif_nie, 
						"compte_bancari":al.compte_bancari,"curs":al.curs,
						"pais":al.pais, "sexe":al.sexe,
						}
				'''el json no accepta aquest tipus de dades."grup_teatre":al.grup_teatre,"data_naixement":al.data_naixement'''
				list_alumnat.append(alumnae)
			alumnat_json = {"Alumnat": list_alumnat}
			return HttpResponse(json.dumps(alumnat_json))
		elif tipus=='xml':
			variables = Context({
						'alumnat': alumnat
						})
			t = loader.get_template('alumnatpage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")		   		
	except:
		raise Http404('Error al generar la pagina')

	
''' mostrar un alumne concret i tots els seus camps en format json/xml'''
def alumnae_jx_page(request, tipus, idAlumne):
	try:
		al = Alumnat.objects.get(id = int(idAlumne))	 
		if tipus=='json':
			list_alumnat = []
			alumnae = {"nom": al.nom, "Tel. personal": al.telefon_personal, 
						"Tel. personal_encarregada":al.telefon_persona_encarregada, 
						"email": al.email, "nif_nie": al.nif_nie, 
						"compte_bancari":al.compte_bancari,"curs":al.curs,
						"pais":al.pais, "sexe":al.sexe
						}
			'''el json no accepta aquest tipus de dades."grup_teatre":al.grup_teatre,"data_naixement":al.data_naixement'''
			list_alumnat.append(alumnae)
			alumnae_json = {"Alumne/a": list_alumnat}
			return HttpResponse(json.dumps(alumnae_json))
		elif tipus=='xml':		    
			variables = Context({
						'alumnae': al
						})
			t = loader.get_template('alumnaepage.xml')			
			c = Context(variables)
    		return HttpResponse(t.render(c), mimetype="application/xml")
	except:
		raise Http404('Error al generar la pagina')


### RESTful API views ###

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.user == request.user

class APIAjuntamentList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Ajuntament
    serializer_class = AjuntamentSerializer

class APIAjuntamentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Ajuntament
    serializer_class = AjuntamentSerializer

class APIGrupTeatreList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = GrupTeatre
    serializer_class = GrupTeatreSerializer

class APIGrupTeatreDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = GrupTeatre
    serializer_class = GrupTeatreSerializer

class APIAlumnatList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Alumnat
    serializer_class = AlumnatSerializer

class APIAlumnatDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Alumnat
    serializer_class = AlumnatSerializer
	




