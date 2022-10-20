from django.test import TestCase

from django_test_parameters_of_models import expected_model
from .models import TestModel


# Create your tests here.
class ExpectedModelForTestModel(expected_model.ExpectedModel):
    __TEST_CHOICES_FOR_CHAR_FIELD = (("test1", "Test 1"), ("2test", "Test 2"))

    id = {"primary_key": True}

    test_char_field = {
        "max_length": 100,
        "null": False,
        "blank": True,
        "choices": __TEST_CHOICES_FOR_CHAR_FIELD,
        "default": "test1",
        "editable": True,
        "help_text": "It test field",
        "primary_key": False,
        "unique": False,
        "verbose_name": "Char field"
    }

    int_field = {
        "verbose_name": "Integer field"
    }


class TestTestModel(TestCase):
    def test_comparing_test_model_with_expected(self):
        self.assertTrue(
            ExpectedModelForTestModel() == TestModel(),
            msg="Expected model equal test model, but returned False"
        )

    def test_incorrect_test_model_with_expected(self):
        incorrect_expected_model = ExpectedModelForTestModel()
        incorrect_expected_model.id = {"primary_key": False}
        self.assertFalse(
            incorrect_expected_model == TestModel(),
            msg="Expected model don't equal test model, but return True"
        )
