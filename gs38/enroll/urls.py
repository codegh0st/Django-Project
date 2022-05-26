from django.urls import path
from enroll import views

urlpatterns = [
    path('enrollapp/', views.showformdata),
    path('successapp/', views.success),
]