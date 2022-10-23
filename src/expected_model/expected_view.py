from django.views import View


class ExpectedView:
    """
    Storage expected field values. Uses for compare real view with expected.
    Expected fields storages same as in view. For compare needs using equal
    operator, like as ExpectedView == RealView
    """
    def __eq__(self, other):
        """
        Compare expected view with real
        
        :return : True, if all fields values of real view equal expected else
        return False
        """
        if isinstance(other, View):
            self_fields_names = list(self.__class__.__dict__.keys())
            self_fields_names = list(filter(
                lambda f: "__" not in f, self_fields_names))

            for field_name in self_fields_names:
                expected_value = getattr(self, field_name)
                real_value = getattr(other, field_name)

                if expected_value != real_value:
                    return False

            return True
