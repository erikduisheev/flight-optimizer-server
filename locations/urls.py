from django.urls import path

from locations.views import LocationsView

urlpatterns = [
    path('locations', LocationsView.as_view())
]
