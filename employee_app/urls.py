from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard, name='dashboard'),
    path('insert/',views.insert_employee, name='insert_employee'),
    path('update/', views.update_employee, name='update_employee'),
    path('delete/', views.delete_employee, name='delete_employee'),
    path('search/', views.search_employee, name='search_employee'),
]
