from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.i18n import JavaScriptCatalog

from .views import IndexView, LoginView, PerfilView, DepoimentoView, UpdateDepoimentoView, DeleteDepoimentoView, \
    TestCoverageView, TestsCoreModelsView, TestsCoreViewsView, TestsBibModelsView, TestsBibViewsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),                              # homepage
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),          # logout
    path('login/', LoginView.as_view(), name='login'),                        # login
    path('perfil/', PerfilView.as_view(), name='perfil'),                     # profile page
    path('social-auth/', include('social_django.urls', namespace='social')),  # social-auth required for Facebook
    path('depoimento/', DepoimentoView.as_view(), name='depoimento'),                 # testimonials CreateView
    path('<int:pk>/update/', UpdateDepoimentoView.as_view(), name='upd_depoimento'),  # testimonials UpdateView
    path('<int:pk>/delete/', DeleteDepoimentoView.as_view(), name='del_depoimento'),  # testimonials DeleteView
    path('coverage/', TestCoverageView.as_view(), name='test_coverage'),                    # tests coverage view
    path('coverage/core_models/', TestsCoreModelsView.as_view(), name='test_core_models'),  # core/models.py coverage
    path('coverage/core_views/', TestsCoreViewsView.as_view(), name='test_core_views'),     # core/views.py coverage
    path('coverage/bib_models/', TestsBibModelsView.as_view(), name='test_bib_models'),     # bib/models.py coverage
    path('coverage/bib_views/', TestsBibViewsView.as_view(), name='test_bib_views'),        # bib/views.py coverage
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
