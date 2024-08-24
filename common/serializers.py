from typing import Any, Dict, List, Tuple

from django.core.exceptions import ValidationError
from django.db import models


def validate_json(data: Dict[str, Any], model_class: models.Model) -> Dict[str, Any]:
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


def model_update(instance: models.Model, fields: List[str], data: Dict[str, Any]) -> Tuple[models.Model, bool]:
    has_updated = False
    update_fields = []

    model_fields = {field.name: field for field in instance._meta.get_fields()}

    for field in fields:
        if field not in data:
            continue

        model_field = model_fields.get(field)

        assert model_field is not None, f"{field} is not part of {instance.__class__.__name__} fields."

        if getattr(instance, field) != data[field]:
            has_updated = True
            update_fields.append(field)
            setattr(instance, field, data[field])

    if has_updated:
        instance.full_clean()
        instance.save(update_fields=update_fields)

    return instance, has_updated
