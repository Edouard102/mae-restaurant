from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("bookings/", include("booking.urls")),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]