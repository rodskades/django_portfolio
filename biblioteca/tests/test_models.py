from django.test import TestCase
from model_mommy import mommy


class AutoresTestCase(TestCase):

    def setUp(self) -> None:
        self.autor = mommy.make('Autores')

    def test_str(self) -> None:
        self.assertEquals(str(self.autor), self.autor.nome)


class EditorasTestCase(TestCase):

    def setUp(self) -> None:
        self.editora = mommy.make('Editoras')

    def test_str(self) -> None:
        self.assertEquals(str(self.editora), self.editora.nome)


class GenerosTestCase(TestCase):

    def setUp(self) -> None:
        self.genero = mommy.make('Generos')

    def test_str(self) -> None:
        self.assertEquals(str(self.genero), self.genero.genero)


class LivrosTestCase(TestCase):

    def setUp(self) -> None:
        self.livro = mommy.make('Livros')

    def test_str(self) -> None:
        self.assertEquals(str(self.livro), self.livro.nome)


class LivrosEditorasTestCase(TestCase):

    def setUp(self) -> None:
        self.livro_editora = mommy.make('LivrosEditoras')

    def test_str(self) -> None:
        le_nome = f'Livro: {self.livro_editora.id_livro} da Editora: {self.livro_editora.id_editora}.'
        self.assertEquals(str(self.livro_editora), le_nome)


class ComplementosTestCase(TestCase):

    def setUp(self) -> None:
        self.comp = mommy.make('Complementos')

    def test_str(self) -> None:
        comp_nome = f'Livro base: {self.comp.id_livro_base} e Livro Complementar: {self.comp.id_livro_complementar}.'
        self.assertEquals(str(self.comp), comp_nome)
