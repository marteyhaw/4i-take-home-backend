import json

from django.db.utils import IntegrityError
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from assets.encoders import AssetDetailEncoder, AssetListEncoder
from assets.models import Asset
from common.errors import json_message_response
from common.serializers import validate_json


@require_http_methods(["GET", "POST"])
def api_list_assets(request: HttpRequest):
    if request.method == "GET":
        assets = Asset.objects.all()
        return JsonResponse(
            {"assets": assets},
            encoder=AssetListEncoder,
        )

    else:
        content = json.loads(request.body)

        errors = validate_json(content, Asset)
        if errors:
            return JsonResponse({"errors": errors}, status=400)

        try:
            asset = Asset.objects.create(**content)
        except IntegrityError:
            return json_message_response("Serial number already exists.", 400)

        return JsonResponse(
            asset,
            encoder=AssetDetailEncoder,
            safe=False,
            status=201,
        )
