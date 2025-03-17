# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# # Create your models here.
#
#
# class Employee(AbstractUser):
#     username = None
#     name = models.CharField(max_length=45, verbose_name='имя', help_text='Введите имя')
#     phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', help_text='Введите номер телефона',
#                                     blank=True, null=True)
#     is_moder = models.BooleanField(default=True, verbose_name="модератор")
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     def __str__(self):
#         return f'{self.email}, {self.name}'
#
#     class Meta:
#         verbose_name = 'сотрудник'
#         verbose_name_plural = "сотрудники"
