from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import Ajuntament, Alumnat, GrupTeatre

class AjuntamentSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='iteatre:ajuntament-detail')
    #user = CharField(read_only=True)
    class Meta:
        model = Ajuntament
        fields = ('url', 'nom', 'telefon', 'email', 'adreca', 'cif')

class AlumnatSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='iteatre:alumnat-detail')
    grup_teatre = HyperlinkedRelatedField(view_name='iteatre:grupteatre-detail')
    user = CharField(read_only=True)
    class Meta:
        model = Alumnat
        fields = ('url', 'nom', 'telefon_personal', 'telefon_persona_encarregada',
         'email', 'nif_nie', 'compte_bancari', 'data_naixement','curs','sexe',
         'pais','ciutat','user','grup_teatre')

class GrupTeatreSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='iteatre:grupteatre-detail')
    ajuntament = HyperlinkedRelatedField(view_name='iteatre:ajuntament-detail')
    user = CharField(read_only=True)
    class Meta:
        model = GrupTeatre
        fields = ('url', 'nom', 'data_comencament', 'data_finalitzacio',
        	'dies_i_horaris','user', 'ajuntament')
