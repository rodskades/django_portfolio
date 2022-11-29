from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


# Model for testimonials that are gonna be displayed on index:
class Depoimentos(models.Model):
    # Current user.
    nome = models.ForeignKey(User, verbose_name=_('Nome'), on_delete=models.DO_NOTHING)
    # Choices for ranking the site.
    nota_choices = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    # The rank.
    nota = models.IntegerField(_('Nota'), choices=nota_choices, help_text=_('Dê uma nota para o site!'), default='5',
                               blank=False)
    # Title for the testimonial
    titulo = models.CharField(_('Título'), max_length=50, help_text=_('Máximo 50 caracteres.'))
    # Testimonial
    comentario = models.TextField(_('Comentário'), max_length=300, help_text=_('Máximo 300 caracteres.'))

    class Meta:
        verbose_name = _('Depoimento')
        verbose_name_plural = _('Depoimentos')

    def __str__(self):
        return self.titulo
