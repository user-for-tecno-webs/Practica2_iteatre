from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

def get_default_user():
    return User.objects.get(pk=1)

class Ajuntament(models.Model):
	nom = models.CharField(max_length=50)
	telefon = models.PositiveIntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	adreca = models.CharField(max_length=60,blank=True, null=True)
	cif = models.CharField(max_length=9,blank=True, null=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.nom

class GrupTeatre(models.Model):
	nom = models.CharField(max_length=50)
	data_comencament = models.DateField(blank=True, null=True)
	data_finalitzacio = models.DateField(blank=True, null=True)
	dies_i_horaris = models.CharField(max_length=60,blank=True, null=True)
	user = models.ForeignKey(User)
	ajuntament = models.ForeignKey(Ajuntament)

	def __unicode__(self):
		return self.nom
		
	def get_absolute_url(self):
		return reverse('iteatre:grupdeteatre_detail', kwargs={'pk': self.pk})
	

class Alumnat(models.Model):

	nom = models.CharField(max_length=50)
	telefon_personal = models.PositiveIntegerField(blank=True, null=True)
	telefon_persona_encarregada = models.PositiveIntegerField(blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	nif_nie = models.CharField(max_length=8,blank=True, null=True)
	compte_bancari = models.CharField(max_length=24,blank=True, null=True)
	data_naixement = models.DateField(blank=True, null=True)
	curs = models.CharField(max_length=15,blank=True, null=True)
	sexe = models.CharField(max_length=15,blank=True, null=True)
	pais = models.CharField(max_length=30,blank=True, null=True)
	ciutat = models.CharField(max_length=30,blank=True, null=True)
	user = models.ForeignKey(User, default = get_default_user)
	grup_teatre = models.ForeignKey(GrupTeatre, null=True, related_name='alumnat')
	
	def __unicode__(self):
		return self.nom

	def get_absolute_url(self):
		return reverse('iteatre:alumnae_detail', kwargs={'pk': self.pk})


""" --- utilitzarem class User builtin en Django, considerant que Professorat i Funcionari gestionaran la info. des de
        la pagina de administracio de django ----

class Professorat(models.Model):
	nom = models.CharField()
	telefon = models.PositiveIntegerField()
	email = models.EmailField()
	nif_nie = models.CharField()
	dataNaixement = models.DateField()
	titulacio = models.TextField(max_length=300)

class Funcionari(models.Model):
	nom = models.CharField()
	telefondirecte = models.PositiveIntegerField()
	emailpersonalajuntament = models.EmailField()
"""
