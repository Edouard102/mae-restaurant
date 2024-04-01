from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_booking, name='add_booking'),
    path('edit/<int:pk>/', views.edit_booking, name='edit_booking'),
    path('delete/<int:pk>/', views.delete_booking, name='cancel_booking'),
    path('booking_list/', views.booking_list, name='booking_list'),
]