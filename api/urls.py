from django.urls import path

from api.views import get_processed_data

urlpatterns = [
    path('process_image/',get_processed_data, name="process_image"),
]