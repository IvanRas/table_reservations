from django import forms

from .models import Order, Table


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ["number", "price", "image", "table_occupiers"]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
