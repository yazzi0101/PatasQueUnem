# Create your tests here.

from django.test import TestCase
from .models import Animal

class AnimalModelTest(TestCase):
    def test_animal_criado_corretamente(self):