from django.urls import path

from restaurant.views import TableCreateView,TableDeleteView, TableDetailView, TableUpdateView, HomeListView
from restaurant.apps import RestaurantConfig

app_name = RestaurantConfig.name

urlpatterns = [
    path('home/<int:pk>/', TableDetailView.as_view(), name='table_detail'),
    path('home/', HomeListView.as_view(), name='home'),
    path('create_blog/', TableCreateView.as_view(), name='table_blog'),
    path('home/<int:pk>/update/', TableUpdateView.as_view(), name='table_update'),
    path('home/<int:pk>/delete/', TableDeleteView.as_view(), name='table_delete')
]