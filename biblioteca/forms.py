from django import forms
from .models import Autor, Livro
from datetime import date
class AutorForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=200)
    nacionalidade = forms.CharField(label="Nacionalidade", max_length=200, required=False)
    def save(self):
        autor = Autor(**self.cleaned_data)
        autor.save()
        return autor

class LivroForm(forms.ModelForm):
    autores = forms.ModelChoiceField(
        queryset=Autor.objects.all(),
        label='Autor',
        empty_label='Selecione um autor'
    )
    class Meta:
        model = Livro
        fields = '__all__'
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'titulo': 'Título',
            'autores': 'Autor',
            'ano_publicacao': 'Ano de Publicação',
            'disponivel': 'Disponível',
            'categorias': 'Categoria(s)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.initial['autores'] = self.instance.autores.first()

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        titulo = " ".join(titulo.split())
        if len(titulo) < 3:
            raise forms.ValidationError("O título deve ter pelo menos 3 caracteres.")
        return titulo

    def clean_ano_publicacao(self):
        ano_publicacao = self.cleaned_data.get('ano_publicacao')
        if ano_publicacao > date.today().year:
            raise forms.ValidationError("O ano de publicação não pode ser futuro.")
        return ano_publicacao