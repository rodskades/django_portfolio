from django.contrib import admin

from .models import Autores, Editoras, Generos, Livros, LivrosEditoras, Complementos


@admin.register(Autores)
class AutoresAdmin(admin.ModelAdmin):
    list_display = ('idautores', 'nome')


@admin.register(Editoras)
class EditorasAdmin(admin.ModelAdmin):
    list_display = ('ideditoras', 'nome')


@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ('idgeneros', 'genero')


@admin.display(description="Páginas")
def get_paginas(obj):
    return obj.paginas


@admin.display(description="Gênero")
def get_genero(obj):
    return obj.id_genero


@admin.display(description="Terminado?")
def get_terminado(obj):
    return obj.terminado


@admin.register(Livros)
class LivrosAdmin(admin.ModelAdmin):
    list_display = ('nome', get_genero, get_paginas, get_terminado)


@admin.register(LivrosEditoras)
class LivrosEditorasAdmin(admin.ModelAdmin):
    list_display = ('idlivros_editoras', 'id_livro', 'id_editora')


@admin.register(Complementos)
class ComplementosAdmin(admin.ModelAdmin):
    list_display = ('idcomplementos', 'id_livro_base', 'id_livro_complementar')
