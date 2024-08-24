import json

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from common.errors import json_message_response
from employees.encoders import EmployeeDetailEncoder, EmployeeListEncoder
from employees.models import Employee


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
        try:
            employee = Employee.objects.create(**content)
        except Exception as e:
            message = f"Bad request. ({e.__class__.__name__})"
            return json_message_response(message, 400)

        return JsonResponse(
            employee,
            encoder=EmployeeDetailEncoder,
            safe=False,
            status=201,
        )
