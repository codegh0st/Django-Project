
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('enrollapp/', views.enroll)
]