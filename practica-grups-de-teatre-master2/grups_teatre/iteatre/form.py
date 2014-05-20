from django.forms import ModelForm
from iteatre.models import Alumnat, GrupTeatre

class AlumnatForm(ModelForm):
    class Meta:
        model = Alumnat 
        #exclude = ('user')

class GrupTeatreForm(ModelForm):
    class Meta:
        model = GrupTeatre
        exclude = ('user')
