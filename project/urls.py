
from django.contrib import admin
from django.urls import path
from app.views import site

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', site)
]
