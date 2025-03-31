from django.conf import settings
from rest_framework import generics, filters, viewsets, permissions, status
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from .services import create_stripe_price, create_stripe_session, create_product_table

from users.forms import UserRegistrationForm
from users.models import User, Payment
from restaurant.models import Table

# Payment

from .forms import UserForm
from .serializers import PaymentSerializer


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
    template_name = "user_list.html"
    context_object_name = "users"

    # def get_queryset(self):
    #     queryset = cache.get('user_queryset')
    #     if not queryset:
    #         queryset = super().get_queryset()
    #         cache.set('user_queryset', queryset, 60 * 2)
    #     return queryset


class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy("user_list")


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "user_form.html"
    success_url = reverse_lazy("users:user_list")


class UserDeleteView(DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy("user_list")


class PaymentList(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = {
        "paid_course": ["exact"],
        "paid_lesson": ["exact"],
        "payment_method": ["exact"],
    }
    ordering_fields = ["payment_date"]
    ordering = ["payment_date"]


class PaymentViewSet(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        global price, product_price
        product_type = serializer.validated_data["product_type"]  # ' table'
        table_id = serializer.validated_data["table_id"]  # ID cnjkf

        if product_type == "tabel":
            product = Table.objects.get(id=table_id)
            product_number = product.number
            product_price = product.price

            # Создаем продукт в Stripe для стола
            stripe_product = create_product_table(product_number)
            price = create_stripe_price(stripe_product.id, product_price)

            product.stripe_price_id = price.id
            product.save()

            # Создаем сессию для оплаты
        session = create_stripe_session(price.id)

        # Сохраняем платеж в базе данных
        payment = serializer.save(
            user=self.request.user,
            amount=product_price,
            session_id=session.id,
            payment_link=session.url,
        )

        return Response(
            {
                "checkout_url": session.url,
                "payment_id": payment.id,
            },
            status=status.HTTP_201_CREATED,
        )
