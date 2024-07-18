from django.contrib import admin
from django.urls import path, include
from blogapp.views import home

urlpatterns = [
    path('', home),  # Basic view for the root URL
    path('admin/', admin.site.urls),
    path('api/', include('blogapp.urls')),
]
