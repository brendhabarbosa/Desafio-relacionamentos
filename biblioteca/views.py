
from django.shortcuts import render, get_object_or_404, redirect
from .models import Livro, Autor
from .forms import AutorForm


def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})


def author_detail(request, author_id):
    autor = get_object_or_404(Autor, id=author_id)

    return render(request, 'biblioteca/author_detail.html', {'autor': autor})


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
