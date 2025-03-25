from django.db import models
from users.models import User

# Create your models here.


class Table(models.Model):
    number = models.CharField(max_length=50, verbose_name="номер стола", help_text="Введите номер стола")
    content = models.TextField(verbose_name="содержимое", help_text="Введите содержимое")
    price = models.CharField(max_length=100, verbose_name='Цена', help_text='Введите цену', default=3000)
    image = models.ImageField(
        upload_to="table_image/",
        blank=True,
        null=True,
        verbose_name="фото",
        help_text="Загрузити фотографию",
    )
    # guest = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name='категория',
    #                              help_text='Введите категорию', blank=True, null=True)
    table_occupiers = models.DateTimeField(verbose_name="занятость стола", default=240)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения", blank=True, null=True)
    # reservation = models.BooleanField(default=False, verbose_name="Бронь")

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"
        ordering = ["number"]


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.SET_NULL, blank=True, null=True)
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
