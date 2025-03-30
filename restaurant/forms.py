from django import forms
from django.core.exceptions import ValidationError


from .models import Order, Table


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["number", "sitting", "price", "image"]

    def clean_number(self):
        number = self.cleaned_data.get("number")
        if number in [table.number for table in Table.objects.all()]:
            raise ValidationError("такой стол уже есть")
        return number

    def clean_sitting(self):
        sitting = self.cleaned_data.get("sitting")
        if sitting > 6:
            raise ValidationError("Не больше 6 мест")
        return sitting


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["table", "time", "date"]
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"), attrs={"class": "form-control", "placeholder": "Выберите дату", "type": "date"}
            ),
        }
