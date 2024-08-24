from django.http import JsonResponse


def json_message_response(message: str, status: int) -> JsonResponse:
    return JsonResponse(
        {
            "message": message,
        },
        status=status,
    )
