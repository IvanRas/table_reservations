from django.conf import settings
from django.core.mail import send_mail

from users.forms import UserRegistrationForm
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from .forms import UserForm

from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)


class RegisterView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        response = super().form_valid(form)

        send_mail(
            subject="Добро пожаловать!",
            message='Спасибо за регистрацию на нашем сайте "__"',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[form.cleaned_data.get("email")],
            fail_silently=False,
        )

        return response


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
