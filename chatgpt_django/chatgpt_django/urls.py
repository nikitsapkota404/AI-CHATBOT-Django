
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', include('chatbotapp.urls')),  # Include app URLs
]
