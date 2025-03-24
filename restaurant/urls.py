from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import (
    HomeListView,
    TableCreateView,
    TableDeleteView,
    TableDetailView,
    TableUpdateView,
    UserCreateView,
    HomeView,
    UserUpdateView,
    UserDeleteView,
    UserListView,
    )

app_name = RestaurantConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name="home"),

    path('user/', UserListView.as_view(), name='user_list'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),

    path("table/table_list/", HomeListView.as_view(), name="table_list"),
    path("table/table_create/", TableCreateView.as_view(), name="table_create"),
    path("table/<int:pk>/update/", TableUpdateView.as_view(), name="table_update"),
    path("table/<int:pk>/delete/", TableDeleteView.as_view(), name="table_delete"),
    path("table/<int:pk>/", TableDetailView.as_view(), name="table_detail"),

    # path('messages/', MessageListView.as_view(), name='messages_list'),
    # path('messages/create/', MessageCreateView.as_view(), name='messages_create'),
    # path('messages/update/<int:pk>/', MessageUpdateView.as_view(), name='messages_update'),
    # path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='messages_delete'),
    #
    # path('newsletter/', NewsLetterListView.as_view(), name='newsletter_list'),
    # path('newsletter/create/', NewsLetterCreateView.as_view(), name='newsletter_create'),
    # path('newsletter/update/<int:pk>/', NewsLetterUpdateView.as_view(), name='newsletter_update'),
    # path('newsletter/delete/<int:pk>/', NewsLetterDeleteView.as_view(), name='newsletter_delete'),
    #
    # path('send-mailing/<int:mailing_id>/', SendMailingView.as_view(), name='send_mailing'),

]
