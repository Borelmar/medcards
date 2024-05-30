from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('clients/new/', views.client_create, name='client_create'),
    path('clients/delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('visits/new/', views.visit_create, name='visit_create'),
    path('clients/<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
]
