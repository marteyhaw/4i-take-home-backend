import json

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from employees.encoders import EmployeeDetailEncoder, EmployeeListEncoder

from .models import Employee


@require_http_methods(["GET", "POST"])
def api_list_employees(request: HttpRequest):
    if request.method == "GET":
        employees = Employee.objects.all()
        return JsonResponse(
            {"employees": employees},
            encoder=EmployeeListEncoder,
        )
    else:
        content = json.loads(request.body)
        employee = Employee.objects.create(**content)
        return JsonResponse(
            employee,
            encoder=EmployeeDetailEncoder,
            safe=False,
            status=201,
        )
