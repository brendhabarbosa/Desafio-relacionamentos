from django.urls import path
from . import views

app_name = 'biblioteca'
urlpatterns = [
    path('listar_livros/', views.BookView.as_view(), name='listar_livros'),
    path('author/<int:pk>/', views.AutorDetailView.as_view(), name='author_detail'),
    path('author_cadastro', views.CreateAutorView.as_view(), name="author_cadastro"),
    path('livro/', views.CreateLivroView.as_view(), name="livro_form"),
    path('livro/<int:pk>/', views.UpdateLivroView.as_view(), name='livro_form'),
    path('livro/<int:pk>/delete/', views.DeleteLivroView.as_view(), name='livro_del'),
    path("sobre/", views.SobreView.as_view(), name="sobre"),
]