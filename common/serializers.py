from typing import Any, Dict

from django.core.exceptions import ValidationError
from django.db import models


def validate_json(data: Dict[str, Any], model_class: models.Model):
    errors = {}

    for field in model_class._meta.fields:
        field_name = field.name
        if field_name in data:
            try:
                field.clean(data[field_name], None)
            except ValidationError as e:
                errors[field_name] = e.messages
        elif not field.blank and not field.has_default() and not field.null:
            errors[field_name] = ["This field is required."]

    return errors
