from django.contrib import admin

from .models import Depoimentos


# Register the Depoimentos model:
@admin.register(Depoimentos)
class DepoimentosAdmin(admin.ModelAdmin):
    list_display = ('titulo', '_autor')
    exclude = ['nome', ]  # Changing the username displayed

    def _autor(self, instance):
        return f'{instance.nome.get_full_name()}'

    def get_queryset(self, request):  # Allowing superusers to see everyone testimonials
        qs = super(DepoimentosAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(autor=request.user)

    def save_model(self, request, obj, form, change):  # Register the name as the current user
        obj.nome = request.user
        super().save_model(request, obj, form, change)
