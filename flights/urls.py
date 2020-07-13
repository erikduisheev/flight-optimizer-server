from django.urls import path

from flights.views import FlightsView

urlpatterns = [
    path('flights', FlightsView.as_view()),
]
