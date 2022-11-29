from django.urls import path

from .views import BibListView

urlpatterns = [
    path('', BibListView.as_view(), name='biblioteca'),
]
