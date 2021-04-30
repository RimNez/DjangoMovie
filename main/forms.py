from django import forms
from .models import *


# add form
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('intitulé', 'réalisateur', 'description', 'dateRéalisation', 'nombreSorties', 'image')
