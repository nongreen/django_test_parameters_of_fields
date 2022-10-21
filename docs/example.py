from django.test import TestCase

from django.db import models
from expected_model import expected_model


class ExampleModel(models.Model):
    id = models.BigAutoField(primary_key=True)

    example_char_field = models.CharField(
        max_length=100,
        verbose_name="sdf",
    )


class ExpectedModelForExample(expected_model.ExpectedModel):
    id = { "primary_key": True }

    example_char_field = {
        "max_length": 100,
        "verbose_name": "sdf"
    }


class ExampleTest(TestCase):
    def test_compare_example_model_with_expected(self):
        self.assertTrue(
            ExampleModel() == ExpectedModelForExample(),
            msg="Some message"
        )
