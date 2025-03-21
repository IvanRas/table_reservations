from django.db import models

# Create your models here.


class Table(models.Model):
    number = models.CharField(max_length=50, verbose_name="номер стола", help_text="Введите номер стола")
    content = models.TextField(verbose_name="содержимое", help_text="Введите содержимое")
    image = models.ImageField(
        upload_to="table_image/",
        blank=True,
        null=True,
        verbose_name="фото",
        help_text="Загрузити фотографию",
    )
    table_occupiers = models.DateTimeField(verbose_name="занятость стола", default=240)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения", blank=True, null=True)
    reservation = models.BooleanField(default=False, verbose_name="Бронь")

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "стол"
        verbose_name_plural = "столы"
        ordering = ["number"]
