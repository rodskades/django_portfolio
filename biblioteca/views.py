from django.views.generic import ListView
from django.utils import translation

from .models import Livros, Complementos


class BibListView(ListView):
    template_name = 'bib_index.html'
    models = Livros
    qs = """
        SELECT l.idlivros, l.nome, g.genero, a.nome AS autor, l.paginas, l.terminado
            FROM biblioteca_livros AS l, biblioteca_generos AS g, biblioteca_autores AS a
            WHERE l.id_genero_id = g.idgeneros AND l.id_autor_id = a.idautores;
        """
    queryset = Livros.objects.raw(qs)
    context_object_name = 'livros'

    qs_le = """
        SELECT l.idlivros, e.nome AS editora
            FROM biblioteca_livros AS l, biblioteca_livroseditoras AS le, biblioteca_editoras AS e
            WHERE l.idlivros = le.id_livro_id AND e.ideditoras = le.id_editora_id;
        """
    editoras = Livros.objects.raw(qs_le)

    qs_com = """
        SELECT c.idcomplementos, l.idlivros, l2.nome AS complemento
            FROM biblioteca_complementos AS c, biblioteca_livros AS l, biblioteca_livros AS l2
            WHERE l.idlivros = c.id_livro_base_id AND l2.idlivros = c.id_livro_complementar_id;
    """
    complementos = Complementos.objects.raw(qs_com)

    livros_com_comp = set(Complementos.objects.values_list('id_livro_base_id'))

    # Translation for other languages:
    lang = translation.get_language()

    extra_context = {'editoras': editoras, 'complementos': complementos, 'list_complementos': livros_com_comp,
                     'lang': lang
                     }

    translation.activate(lang)

    # Pagination for the table:
    paginate_by = 7

