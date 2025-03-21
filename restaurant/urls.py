from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import (
    HomeListView,
    TableCreateView,
    TableDeleteView,
    TableDetailView,
    TableUpdateView,
)

app_name = RestaurantConfig.name

urlpatterns = [
    path("tabel_create/", TableCreateView.as_view(), name="tabel_create"),
    path("home/", HomeListView.as_view(), name="home"),
    path("home/<int:pk>/update/", TableUpdateView.as_view(), name="table_update"),
    path("home/<int:pk>/delete/", TableDeleteView.as_view(), name="table_delete"),
    path("home/<int:pk>/", TableDetailView.as_view(), name="table_detail"),
]
