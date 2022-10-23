from django.test import TestCase
from expected_classes import expected_view

from .views import ListViewForTest
from .models import TestModel


class ExpectedTestView(expected_view.ExpectedView):
    template_name = "Test template"
    page_kwarg = "page"
    paginate_by = 5
    model = TestModel
    context_object_name = "Test name"


class TestTestView(TestCase):
    def test_compare_expected_view_with_real(self):
        self.assertTrue(
            ExpectedTestView() == ListViewForTest(),
            msg="Got correct view, but returned False"
        )

    def test_compare_incorrect_real_view_with_expected(self):
        expected_test_view = ExpectedTestView()
        expected_test_view.paginate_by = 10

        self.assertFalse(
            expected_test_view == ListViewForTest(),
            msg="Got incorrect view, but returned True"
        )
