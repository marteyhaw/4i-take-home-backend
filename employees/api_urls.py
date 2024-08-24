from django.urls import path

from employees.api_views import api_list_employees, api_show_employee

urlpatterns = [
    path("", api_list_employees, name="api_list_or_create_employees"),
    path("<int:id>/", api_show_employee, name="api_show_employee"),
]
