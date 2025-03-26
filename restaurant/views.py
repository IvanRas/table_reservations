from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

# from .services import get_products_by_category, CategoryService
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from restaurant.models import Order, Table

from .forms import OrderForm, TableForm
from .permissions import IsModerator

# Create your views here.


# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeListView(ListView):
    model = Table
    template_name = "restaurant/base.html"
    context_object_name = "tables"


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = "restaurant/table_create.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


class TableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Table
    template_name = "restaurant/table_create.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


# @method_decorator(cache_page(60 * 15), name='dispatch')
class TableDetailView(LoginRequiredMixin, DetailView):
    model = Table
    template_name = "restaurant/table_detail.html"
    context_object_name = "table"
    permission_classes = [IsModerator]

    # def get_queryset(self):
    #     queryset = cache.get('category_queryset')
    #     if not queryset:
    #         queryset = super().get_queryset()
    #         cache.set('category_queryset', queryset, 60 * 15)
    #     return queryset


class TableDeleteView(LoginRequiredMixin, DeleteView):
    model = Table
    template_name = "restaurant/table_delete.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


class HomeView(TemplateView):
    template_name = "home.html"


class OrderListView(ListView):
    model = Order
    template_name = "restaurant/order_list.html"
    context_object_name = "table"


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = "restaurant/order_create.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Order
    template_name = "restaurant/order_create.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


# @method_decorator(cache_page(60 * 15), name='dispatch')
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "restaurant/order_detail.html"
    context_object_name = "table"
    permission_classes = [IsModerator]


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "restaurant/order_delete.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]
