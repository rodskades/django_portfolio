from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth.models import User


# Testing for the CreateView of the testimonials:
class DepoimentoViewTestCase(TestCase):

    def setUp(self) -> None:
        self.dados = {  # Testing data.
            'nota': 1,
            'titulo': 'Título',
            'comentario': 'Comentário do usuário'
        }
        # Test-only user:
        self.test_user = User.objects.create_user(username='teste', email='teste@gmail.com', password='Teste13579531')
        self.cliente = Client()

    def test_form_valid(self) -> None:
        self.cliente.login(username='teste', password='Teste13579531')            # Login for the test user.
        request = self.cliente.post(reverse_lazy('depoimento'), data=self.dados)  # Submit the data.
        self.assertEquals(request.status_code, 302)                               # Verifying the status code.


# Testing for the UpdateView of the testimonials:
class UpdateDepoimentoViewTestCase(TestCase):

    def setUp(self) -> None:
        self.dados = {  # Testing data.
            'nota': 1,
            'titulo': 'Título',
            'comentario': 'Comentário do usuário'
        }
        # Test-only user:
        self.test_user = User.objects.create_user(username='teste', email='teste@gmail.com', password='Teste13579531')
        self.cliente = Client()

    def test_form_valid(self) -> None:
        self.cliente.login(username='teste', password='Teste13579531')  # Login for the test user.
        self.cliente.post(reverse_lazy('depoimento'), data=self.dados)  # Submit the data.
        request = self.cliente.post('/1/update/', data=self.dados)      # Update the submitted data.
        self.assertEquals(request.status_code, 302)                     # Verifying the status code.


# Testing for the DeleteView for the testimonials:
class DeleteDepoimentoViewTestCase(TestCase):

    def setUp(self) -> None:
        self.dados = {  # Testing data.
            'nota': 1,
            'titulo': 'Título',
            'comentario': 'Comentário do usuário'
        }
        # Test-only user:
        self.test_user = User.objects.create_user(username='teste', email='teste@gmail.com', password='Teste13579531')
        self.cliente = Client()

    def test_form_valid(self) -> None:
        self.cliente.login(username='teste', password='Teste13579531')  # Login for the test user
        self.cliente.post(reverse_lazy('depoimento'), data=self.dados)  # Submit the data.
        request = self.cliente.post('/1/delete/')                       # Delete the submitted data.
        self.assertEquals(request.status_code, 302)                     # Verifying the status code.
