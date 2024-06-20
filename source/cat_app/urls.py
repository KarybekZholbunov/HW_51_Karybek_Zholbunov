from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cat/<int:cat_id>/', views.cat_info, name='cat_info'),
]