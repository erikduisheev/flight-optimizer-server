from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from flight_optimizer.cli import FlightOptimizer


class FlightsView(APIView):

    def get(self, request):
        departure = request.query_params.get('from')
        destinations = request.query_params.getlist('to')

        try:
            optimizer = FlightOptimizer(departure, destinations)
            flights = optimizer.process()
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            destinations = [
                {
                    'city': flight.destination.city.name,
                    'airport': flight.destination.airport.name,
                    'price': flight.price,
                    'distance': f'{flight.distance:.0f}',
                    'price_per_km': f'{flight.price_per_kilometer:.2f}',
                    'is_reachable': flight.is_found
                }
                if flight.is_found else
                {
                    'city': flight.destination.city.name,
                    'is_reachable': flight.is_found
                }
                for flight in flights
            ]

            response = {
                'departure': {
                    'city': flights[0].departure.city.name,
                    'airport': flights[0].departure.airport.name
                },
                'destinations': destinations
            }
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response, status=status.HTTP_200_OK)
