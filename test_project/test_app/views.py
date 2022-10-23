from django.views.generic import ListView

from .models import TestModel


class ListViewForTest(ListView):
    template_name = "Test template"
    page_kwarg = "page"
    paginate_by = 5
    model = TestModel
    context_object_name = "Test name"
