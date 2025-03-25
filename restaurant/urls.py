from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import (
    HomeListView,
    TableCreateView,
    TableDeleteView,
    TableDetailView,
    TableUpdateView,
    HomeView,
)

app_name = RestaurantConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path("table/table_list/", HomeListView.as_view(), name="table_list"),
    path("table/table_create/", TableCreateView.as_view(), name="table_create"),
    path("table/update/<int:pk>/", TableUpdateView.as_view(), name="table_update"),
    path("table/delete/<int:pk>/", TableDeleteView.as_view(), name="table_delete"),
    path("table/<int:pk>/", TableDetailView.as_view(), name="table_detail"),

]
