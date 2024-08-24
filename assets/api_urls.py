from django.urls import path

from assets.api_views import api_list_assets

urlpatterns = [
    path("", api_list_assets, name="api_list_or_create_assets"),
]
