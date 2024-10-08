import json

from django.db.utils import IntegrityError
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from common.serializers import model_update, validate_json
from common.utils import json_message_response
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

        errors = validate_json(content, Employee)
        if errors:
            return JsonResponse({"errors": errors}, status=400)

        try:
            employee = Employee.objects.create(**content)
        except IntegrityError:
            return json_message_response("Email or telephone number is already taken.", 400)

        return JsonResponse(
            employee,
            encoder=EmployeeDetailEncoder,
            safe=False,
            status=201,
        )


@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_employee(request: HttpRequest, id: int):
    if request.method == "GET":
        try:
            employee = Employee.objects.get(id=id)
            return JsonResponse(
                employee,
                encoder=EmployeeDetailEncoder,
                safe=False,
            )
        except Employee.DoesNotExist:
            return json_message_response("Invalid employee id.", 404)

    elif request.method == "DELETE":
        count, _ = Employee.objects.filter(id=id).delete()
        if count > 0:
            return json_message_response("Employee deletion successful.", 200)
        else:
            return json_message_response("Employee deletion failed.", 400)

    else:
        content = json.loads(request.body)
        try:
            employee = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return json_message_response("Invalid employee id.", 404)

        props = ["first_name", "last_name", "email", "telephone", "bio", "union"]
        employee, _ = model_update(employee, props, content)

        return JsonResponse(
            employee,
            encoder=EmployeeDetailEncoder,
            safe=False,
        )
