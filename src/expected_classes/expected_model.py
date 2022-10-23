from django.db import models


class ExpectedModel:
    """
    Storage expected parameters of fields of django.models.Model.
    Example class-inheritance:
    class Example(ExpectedModel):
        id = {"primary_key": True}
    Usage: Example == model.Model
    """
    def __eq__(self, other):
        """
        Return True, if all parameters of fields equal expected parameters
        """
        if isinstance(other, models.Model):
            self_fields_names = list(self.__class__.__dict__.keys())
            self_fields_names = list(filter(
                lambda f: "__" not in f, self_fields_names))

            for field_name in self_fields_names:
                expected_parameters = getattr(self, field_name)
                compared_field = other._meta.get_field(field_name)

                if not self._compare_expected_parameters_with_real(
                    expected_parameters,
                    compared_field
                ):
                    return False

            return True

    @classmethod
    def _compare_expected_parameters_with_real(
            cls, expected_parameters: dict,
            compared_field: models.Field
    ):
        """
        Compare an expected parameter with real.

        :param expected_parameters: The dict expected parameters look like
            `{"primary_key": True}`
        :param compared_field: The django.models.Field from real model. Uses for
        getting parameters for compare
        :return True if any parameter equal expected parameter.
        """
        for parameter_name, expected_value in expected_parameters.items():
            real_parameter_value = getattr(compared_field, parameter_name)
            if real_parameter_value != expected_value:
                return False

        return True
