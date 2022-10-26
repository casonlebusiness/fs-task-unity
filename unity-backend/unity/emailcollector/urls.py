from django.urls import path
from . import views

urlpatterns = [
    path('api', views.EmailAPI.as_view(), name='Email APIS'),
    path('reports', views.reports, name='Email Reports')
]