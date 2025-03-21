from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# from .services import get_products_by_category, CategoryService
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from restaurant.models import Table

# Create your views here.


# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeListView(ListView):
    model = Table
    template_name = "table/base.html"
    context_object_name = "table"


class TableCreateView(CreateView):
    model = Table
    template_name = "table/table_form.html"
    success_url = reverse_lazy("restaurant:home")

    def get_queryset(self):
        if self.request.user.groups.filter(name="moderators").exists() or self.request.user.is_staff:
            return Table.objects.all()


class TableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Table
    template_name = "table/table_form.html"
    success_url = reverse_lazy("restaurant:home")

    def get_queryset(self):
        if self.request.user.groups.filter(name="moderators").exists() or self.request.user.is_staff:
            return Table.objects.all()


# @method_decorator(cache_page(60 * 15), name='dispatch')
class TableDetailView(LoginRequiredMixin, DetailView):
    model = Table
    template_name = "table/table_detail.html"
    context_object_name = "table"

    # def get_queryset(self):
    #     queryset = cache.get('category_queryset')
    #     if not queryset:
    #         queryset = super().get_queryset()
    #         cache.set('category_queryset', queryset, 60 * 15)
    #     return queryset

    def get_queryset(self):
        if self.request.user.groups.filter(name="moderators").exists() or self.request.user.is_staff:
            return Table.objects.all()


class TableDeleteView(LoginRequiredMixin, DeleteView):
    model = Table
    template_name = "table/table_delete.html"
    success_url = reverse_lazy("restaurant:home")

    def get_queryset(self):
        if self.request.user.groups.filter(name="moderators").exists() or self.request.user.is_staff:
            return Table.objects.all()
