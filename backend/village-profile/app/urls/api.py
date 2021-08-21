from django.urls import path

from app.views import api_controller
from app.views.settings import collector_controller

urlpatterns = [
    path('wards/', api_controller.get_wards),
    path('bastis/', api_controller.get_bastis),
    path('collectors/', api_controller.get_collectors),


    path('update/collector/<int:id>', collector_controller.update_collector),
]
