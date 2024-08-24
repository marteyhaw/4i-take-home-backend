from django.urls import path

from assets.api_views import api_list_assets, api_show_asset

urlpatterns = [
    path("", api_list_assets, name="api_list_or_create_assets"),
    path("<int:id>/", api_show_asset, name="api_show_asset"),
]
