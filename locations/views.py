from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from flight_optimizer.cli import FlightOptimizer


class LocationsView(APIView):

    def get(self, request):
        departure = request.query_params.get('city')

        try:
            flight_optimizer = FlightOptimizer(departure, departure)
            cities = flight_optimizer.get_city(departure)

        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = {
                "city": cities.input_name,
                "possible_cities": [
                    {
                        "city": city[0],
                        "country": city[1]
                    }
                    for city in cities.correct_name_options
                ]
            }
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(response, status=status.HTTP_200_OK)
