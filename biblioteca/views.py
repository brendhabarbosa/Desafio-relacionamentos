
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Livro, Autor
from .forms import AutorModelForm, LivroModelForm
from django.urls import reverse_lazy, reverse
class BookView(ListView):
    model = Livro
    template_name = "biblioteca/listar_livros.html"
    context_object_name = "livros"
    queryset = Livro.objects.order_by("titulo")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_livros"] = Livro.objects.count()
        context["livros_disponiveis"] = Livro.objects.filter(
            disponivel=True
        ).count()

        return context

class AutorDetailView(DetailView):
    model = Autor
    template_name = "biblioteca/author_detail.html"

class CreateAutorView(CreateView):
    model = Autor
    form_class = AutorModelForm
    template_name = "biblioteca/author_cadastro.html"
    def get_success_url(self):
        return reverse(
            "biblioteca:author_detail",
            kwargs={"pk": self.object.pk}
        )

class CreateLivroView(CreateView):
    model = Livro
    form_class = LivroModelForm
    template_name = "biblioteca/livro_form.html"
    success_url = reverse_lazy("biblioteca:listar_livros")

class UpdateLivroView(UpdateView):
    model = Livro
    form_class = LivroModelForm
    template_name = "biblioteca/livro_form.html"
    success_url = reverse_lazy("biblioteca:listar_livros")

class DeleteLivroView(DeleteView):
    model = Livro
    template_name = "biblioteca/livro_confirm_delete.html"
    success_url = reverse_lazy("biblioteca:listar_livros")

class SobreView(TemplateView):
    template_name = "biblioteca/sobre.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["total_livros"] = Livro.objects.count()
        context["livros_disponiveis"] = Livro.objects.filter(
            disponivel=True
        ).count()

        return context