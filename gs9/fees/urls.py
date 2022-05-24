from django.contrib import admin
from django.urls import path
from fees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('feesdj/', views.fees_django),
    path ('feespy/', views.fees_python),
]