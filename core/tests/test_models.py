from django.test import TestCase
from model_mommy import mommy


# Testing the testimonials model:
class DepoimentosTestCase(TestCase):

    def setUp(self) -> None:
        self.depoimento = mommy.make('Depoimentos')  # Mommy will generate a random testimonial for the test.

    def test_str(self):
        self.assertEquals(str(self.depoimento), self.depoimento.titulo)  # Checking if str method is working properly.
