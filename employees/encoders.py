from common.encoders import ModelEncoder
from employees.models import Employee


class EmployeeListEncoder(ModelEncoder):
    model = Employee
    properties = ["first_name", "last_name", "email", "telephone", "bio", "union"]


class EmployeeDetailEncoder(ModelEncoder):
    model = Employee
    properties = ["first_name", "last_name", "email", "telephone", "bio", "union"]
