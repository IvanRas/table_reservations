
# from .services import get_products_by_category, CategoryService
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from restaurant.models import Table


# Create your views here.

# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeListView(ListView):
    model = Table
    template_name = 'catalog/base.html'
    context_object_name = 'products'


class TableCreateView(CreateView):
    model = Table
    # form_class = ProductForm
    # template_name = 'catalog/product_form.html'
    # success_url = reverse_lazy('catalog:home')


class TableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Table
    # form_class = ProductForm
    # template_name = 'catalog/product_form.html'
    # success_url = reverse_lazy("catalog:home")

    # def get_form_class(self):
    #     if self.request.user.is_superuser:
    #         return ProductForm
    #     if self.request.user.has_perm("catalog.can_unpublish_product"):
    #         return ProductModeratorForm
    #     if self.request.user.has_perm("catalog.remove_any_product"):
    #         return ProductModeratorForm
    #     return ProductForm


# @method_decorator(cache_page(60 * 15), name='dispatch')
class TableDetailView(LoginRequiredMixin, DetailView):
    model = Table
    # template_name = 'catalog/product_detail.html'
    # context_object_name = 'product'

    # def get_queryset(self):
    #     queryset = cache.get('category_queryset')
    #     if not queryset:
    #         queryset = super().get_queryset()
    #         cache.set('category_queryset', queryset, 60 * 15)
    #     return queryset


class TableDeleteView(LoginRequiredMixin,DeleteView):
    model = Table
    # template_name = 'catalog/product_delete.html'
    # success_url = reverse_lazy('catalog:home')
