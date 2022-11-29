# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autores(models.Model):
    idautores = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Editoras(models.Model):
    ideditoras = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=80)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'


class Generos(models.Model):
    idgeneros = models.AutoField(primary_key=True)
    genero = models.CharField('Gênero', max_length=50)

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'


class Livros(models.Model):
    idlivros = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', max_length=150)
    id_genero = models.ForeignKey(Generos, on_delete=models.DO_NOTHING)
    id_autor = models.ForeignKey(Autores, on_delete=models.DO_NOTHING)
    paginas = models.IntegerField('Páginas')
    terminado = models.CharField('Concluído?', max_length=10)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


class LivrosEditoras(models.Model):
    idlivros_editoras = models.AutoField(primary_key=True)
    id_livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
    id_editora = models.ForeignKey(Editoras, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Livro: {self.id_livro} da Editora: {self.id_editora}.'

    class Meta:
        verbose_name = 'Livro-Editora'
        verbose_name_plural = 'Livros-Editoras'


class Complementos(models.Model):
    idcomplementos = models.AutoField(primary_key=True)
    id_livro_base = models.ForeignKey(Livros, on_delete=models.DO_NOTHING, related_name='LivroBase')
    id_livro_complementar = models.ForeignKey(Livros, on_delete=models.DO_NOTHING, related_name='LivroComplemento')

    def __str__(self):
        return f'Livro base: {self.id_livro_base} e Livro Complementar: {self.id_livro_complementar}.'

    class Meta:
        verbose_name = 'Complemento'
        verbose_name_plural = 'Complementos'
