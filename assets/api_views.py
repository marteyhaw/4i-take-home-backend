import json

from django.db.utils import IntegrityError
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_http_methods

from assets.encoders import AssetDetailEncoder, AssetListEncoder
from assets.models import Asset
from common.serializers import model_update, validate_json
from common.utils import json_message_response


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


@require_http_methods(["GET", "DELETE", "PUT"])
def api_show_asset(request: HttpRequest, id: int):
    if request.method == "GET":
        try:
            asset = Asset.objects.get(id=id)
            return JsonResponse(
                asset,
                encoder=AssetDetailEncoder,
                safe=False,
            )
        except Asset.DoesNotExist:
            return json_message_response("Invalid asset id.", 404)

    elif request.method == "DELETE":
        count, _ = Asset.objects.filter(id=id).delete()
        if count > 0:
            return json_message_response("Asset deletion successful.", 200)
        else:
            return json_message_response("Asset deletion failed.", 400)

    else:
        content = json.loads(request.body)
        try:
            asset = Asset.objects.get(id=id)
        except Asset.DoesNotExist:
            return json_message_response("Invalid asset id.", 404)

        props = ["asset_name", "serial_number", "price", "color", "description", "certification"]
        asset, _ = model_update(asset, props, content)

        return JsonResponse(
            asset,
            encoder=AssetDetailEncoder,
            safe=False,
        )
