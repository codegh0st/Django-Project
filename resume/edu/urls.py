from django.urls import path
from edu import views
urlpatterns = [
    path('skills/', views.skill, name='skills'),
]
