
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from .models import Livro, Autor
from .forms import AutorForm, LivroForm


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})


def author_detail(request, author_id):
    autor = get_object_or_404(Autor, id=author_id)
    livros = autor.livros.all()

    return render(request, 'biblioteca/author_detail.html', {'autor': autor, 'livros': livros,})


def author_cadastro(request):
    if request.method == "POST":
        form = AutorForm(request.POST)

        if form.is_valid():
            autor = form.save()
            return redirect(
                'biblioteca:author_detail',
                author_id=autor.id
            )
    else:
        form = AutorForm()

    return render(
        request,
        'biblioteca/author_cadastro.html',
        {'form': form}
    )

def create_edit_livro(request, pk =None):
    livro = get_object_or_404(Livro, pk=pk) if pk else None
    if request.method == 'POST':
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            with transaction.atomic():
                livro = form.save(commit=False)
                livro.save()
                livro.autores.set([form.cleaned_data['autores']])
            autor = livro.autores.first()
            return redirect('biblioteca:author_detail', author_id=autor.pk)
    else:
        form = LivroForm(instance=livro)
    context = {
        'form': form,
        'titulo_pagina': 'Editar livro' if livro else 'Novo livro',
        'texto_botao': 'Salvar alterações' if livro else 'Novo livro',}
    return render(request, 'biblioteca/livro_form.html', context)