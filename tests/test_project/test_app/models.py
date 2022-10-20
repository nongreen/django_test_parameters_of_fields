from django.db import models


# Create your models here.
class TestModel(models.Model):
    TEST_CHOICES_FOR_CHAR_FIELD = (("test1", "Test 1"), ("2test", "Test 2"))

    id = models.BigAutoField(primary_key=True)

    test_char_field = models.CharField(
        max_length=100,
        null=False,
        blank=True,
        choices=TEST_CHOICES_FOR_CHAR_FIELD,
        default="test1",
        editable=True,
        help_text="It test field",
        primary_key=False,
        unique=False,
        verbose_name="Char field"
    )
    int_field = models.IntegerField(
        verbose_name="Integer field"
    )

    def __str__(self):
        return str(id)
