from assets.models import Asset
from common.encoders import ModelEncoder


class AssetListEncoder(ModelEncoder):
    model = Asset
    properties = ["id", "asset_name", "serial_number", "price", "color", "description", "certification"]


class AssetDetailEncoder(ModelEncoder):
    model = Asset
    properties = ["id", "asset_name", "serial_number", "price", "color", "description", "certification"]
