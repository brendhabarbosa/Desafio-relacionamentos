from django import forms 
from .models import Autor 

class AutorForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=200)
    nacionalidade = forms.CharField(label="Nacionalidade", max_length=200, required=False)
    def save(self):
        autor = Autor(**self.cleaned_data)
        autor.save()
        return autor
