from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext as _
from django.utils import translation

from .models import Depoimentos


# ListView for the index, where testimonials of the site are displayed:
class IndexView(ListView):
    template_name = 'index.html'
    models = Depoimentos
    queryset = Depoimentos.objects.all()
    context_object_name = 'depoimentos'
    # Translation for other languages:
    lang = translation.get_language()
    extra_context = {'lang': lang}
    translation.activate(lang)


# Profile view, requires to be logged in:
class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'perfil.html'
    # Translation for other languages:
    lang = translation.get_language()
    extra_context = {'lang': lang}
    translation.activate(lang)


# The login view:
class LoginView(TemplateView):
    template_name = 'login.html'
    # Translation for other languages:
    lang = translation.get_language()
    extra_context = {'lang': lang}
    translation.activate(lang)


# The testimonials CreateView, requires to be logged in:
class DepoimentoView(LoginRequiredMixin, CreateView):
    model = Depoimentos
    template_name = 'depoimento_form.html'
    fields = ['nota', 'titulo', 'comentario']  # No name is provided since the current user name is gonna be used.
    success_url = '/#depoimentos'  # Trying to redirect the user to the specific testimonials section.
    lang = translation.get_language()
    extra_context = {'lang': lang}
    translation.activate(lang)

    def form_valid(self, form, *args, **kwargs):
        form.instance.nome = self.request.user
        messages.success(self.request, _('Depoimento enviado com sucesso!'))  # Success message if the form is valid.
        return super(DepoimentoView, self).form_valid(form, *args, **kwargs)


# The testimonials UpdateView, requires to be logged in:
class UpdateDepoimentoView(LoginRequiredMixin, UpdateView):
    model = Depoimentos
    template_name = 'depoimento_form.html'
    fields = ['nota', 'titulo', 'comentario']
    success_url = '/#depoimentos'
    # Translation for other languages:
    lang = translation.get_language()
    extra_context = {'lang': lang}
    translation.activate(lang)

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, _('Depoimento atualizado com sucesso!'))  # Success message if the form is valid.
        return super(UpdateDepoimentoView, self).form_valid(form, *args, **kwargs)


# The testimonials DeleteView, requires to be logged in:
class DeleteDepoimentoView(LoginRequiredMixin, DeleteView):
    model = Depoimentos
    template_name = 'depoimento_del.html'
    success_url = '/#depoimentos'
    # Translation for other languages:
    lang = translation.get_language()
    extra_context = {'lang': lang}
    translation.activate(lang)

    def form_valid(self, form, *args, **kwargs):
        messages.success(self.request, _('Depoimento deletado com sucesso!'))
        return super(DeleteDepoimentoView, self).form_valid(form, *args, **kwargs)


# Tests Coverage views.
# I decided to keep these in core instead of a new app, it seemed unnecessary to create a new app just for this...
class TestCoverageView(TemplateView):
    template_name = 'coverage.html'


class TestsCoreModelsView(TemplateView):
    template_name = 'tests_core_models_py.html'


class TestsCoreViewsView(TemplateView):
    template_name = 'tests_core_views_py.html'


class TestsBibModelsView(TemplateView):
    template_name = 'tests_bib_models_py.html'


class TestsBibViewsView(TemplateView):
    template_name = 'tests_bib_views_py.html'
