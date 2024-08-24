from django.urls import path

from employees.api_views import api_list_employees

urlpatterns = [
    path("", api_list_employees, name="api_list_or_create_employees"),
]
