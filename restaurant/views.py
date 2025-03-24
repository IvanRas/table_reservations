from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import UserForm, TableForm


# from .services import get_products_by_category, CategoryService
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView, TemplateView,
)

from restaurant.models import Table
from users.models import User
from .permissions import IsModerator


# Create your views here.


# @method_decorator(cache_page(60 * 15), name='dispatch')
class HomeListView(ListView):
    model = Table
    template_name = "table/base.html"
    context_object_name = "table"


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = "table/table_create.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


class TableUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Table
    template_name = "table/table_create.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


# @method_decorator(cache_page(60 * 15), name='dispatch')
class TableDetailView(LoginRequiredMixin, DetailView):
    model = Table
    template_name = "table/table_detail.html"
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
    template_name = "table/table_delete.html"
    success_url = reverse_lazy("restaurant:home")
    permission_classes = [IsModerator]


class HomeView(TemplateView):
    template_name = 'home.html'


# Create your views here.

# CRUD для получателей (Recipient)


# @method_decorator(cache_page(60 * 2), name='dispatch')


class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

    # def get_queryset(self):
    #     queryset = cache.get('user_queryset')
    #     if not queryset:
    #         queryset = super().get_queryset()
    #         cache.set('user_queryset', queryset, 60 * 2)
    #     return queryset


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user_list')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'user_form.html'
    success_url = reverse_lazy('user_list')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return UserForm
        if self.request.user.has_perm("catalog.can_unpublish_product"):
            return UserForm
        if self.request.user.has_perm("catalog.remove_any_product"):
            return UserForm
        return UserForm


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_delete.html'
    success_url = reverse_lazy('user_list')
