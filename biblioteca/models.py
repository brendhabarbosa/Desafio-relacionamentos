from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, RegexValidator
from datetime import date
class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    #autor = models.ForeignKey(Autor, related_name='books', on_delete=models.CASCADE)
    autores = models.ManyToManyField(Autor, related_name='livros', blank=True)
    ano_publicacao = models.IntegerField(validators=[MinValueValidator(1450), MaxValueValidator(date.today().year)])
    disponivel = models.BooleanField(default=True)
    categorias = models.ManyToManyField(Categoria, blank=True)
    paginas = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5000)])
    isbn = models.CharField(max_length=13, validators=[RegexValidator(r'^\d{13}$')])
    def __str__(self):
        return self.titulo

    def get_autores(self):
       return ", ".join([autor.nome for autor in self.autores.all()])
