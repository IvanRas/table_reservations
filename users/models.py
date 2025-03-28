from django.contrib.auth.models import AbstractUser
from django.db import models
# from restaurant.models import Order

# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Эл.почта")
    name = models.CharField(max_length=45, verbose_name="имя", help_text="Введите имя")

    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона",
        blank=True,
        null=True,
    )
    is_moder = models.BooleanField(default=False, verbose_name="модератор")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}, {self.name}"

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "Пользователи"


# class Payment(models.Model):
#     PAYMENT_METHODS = [
#         ("cash", "Наличными"),
#         ("transfer", "Перевод на счет"),
#     ]
#
#     user = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         verbose_name="пользователь",
#         blank=True,
#         null=True,
#         help_text="Введите пользователя",
#     )
#     payment_date = models.DateTimeField(auto_now_add=True)
#     paid_course = models.ForeignKey(
#         Order,
#         on_delete=models.SET_NULL,
#         related_name="payments",
#         null=True,
#         blank=True,
#         verbose_name="Оплачиваемый заказ",
#     )
#
#     amount = models.DecimalField(
#         max_digits=10, decimal_places=2, verbose_name="Сумма платежа"
#     )
#     session_id = models.CharField(
#         max_length=255,
#         verbose_name="Id заказа",
#         blank=True,
#         null=True,
#         help_text="Введите Id заказа",
#     )
#     payment_link = models.URLField(
#         max_length=400, null=True, blank=True, verbose_name="Ссылка на платеж"
#     )
#     payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS)
#
#     def __str__(self):
#         return f"Payment of {self.amount} by {self.user.email} on {self.payment_date}"
#
#     class Meta:
#         verbose_name = "Платеж"
#         verbose_name_plural = "Платежи"
