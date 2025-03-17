from django.db import models

# Create your models here.


class Table(models.Model):
    number = models.CharField(max_length=250, verbose_name='номер стола', help_text='Введите номер стола')
    content = models.TextField(verbose_name='содержимое', help_text='Введите содержимое')
    image = models.ImageField(upload_to='table_image/', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузити фотографию')
    created_at = models.DateField(verbose_name='дата создания', help_text='Введите датe создания', blank=True,
                                  null=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', blank=True, null=True)
    reservation = models.BooleanField(default=False, verbose_name="Доступность")

    def __str__(self):
        return f'{self.number}'

    class Meta:
        verbose_name = 'стол'
        verbose_name_plural = 'столы'
        ordering = ['number']