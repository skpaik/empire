from rest_framework.views import *

from api.models import Starship
from api.serializers import StarshipSerializer
from api.services import SwapiService


class SpeciesView(APIView):
    def __int__(self):
        self.swapiService = SwapiService()

    # Does something to get xwings
    def get(self, request, **kwargs):
        swapi_service = SwapiService()

        query_params = request.query_params

        species_list = []

        starship_id = query_params.get('starship_id')
        creator = query_params.get('creator')

        if starship_id:
            species = swapi_service.get_species_by_starship_id(starship_id)
            species_list.extend(species)
        if creator:
            species = swapi_service.get_species_by_creator_name(creator)
            species_list.extend(species)

        data = {
            "success": True,
            "species": list(set(species_list))
        }

        return Response(data)

    def post(self, request, **kwargs):
        id = request.data.get("id")
        if not isinstance(id, int):
            return Response("Bad request")
        # XWing2.objects.create(**request.data)
        return Response("ok")


class EvacuateView(APIView):
    # Does something to get xwings
    lookup_url_kwarg_starship_id = "starship_id"

    lookup_url_kwarg_planet_id_or_name = "planet_id_or_name"

    def get(self, request, **kwargs):
        swapi_service = SwapiService()

        starship_id = self.kwargs.get(self.lookup_url_kwarg_starship_id)

        planet_id_or_name = self.kwargs.get(self.lookup_url_kwarg_planet_id_or_name)

        evacuation_details = swapi_service.get_evacuation_details(starship_id, planet_id_or_name)

        data = {
            "evacuation_success": True,
            "message": "Evacuated " + str(evacuation_details.get(
                "evacuation_units")) + " units from planet " + evacuation_details.get(
                "planet_name") + " using starship " + evacuation_details.get("starship_name") + "."
        }

        return Response(data)

    def post(self, request, **kwargs):
        '''
        {
          "planet_id": 1,
          "starship_id": 9,
          "units": 1000
        }
       :param request:
        :param kwargs:
        :return:
        '''
        # req_data = request.data
        # planet_id = req_data.get("planet_id")
        # starship_id = req_data.get("starship_id")

        serializer = StarshipSerializer(data=request.data)
        # print(serializer.__dict__)
        #  serializer.data
        #  serializer.data
        print(serializer.initial_data)

        if not serializer.is_valid():
            return Response("Bad request")

        print(serializer.initial_data)
        # StartShip.objects.create(**req_data)

        serializer.save()

        data = {
            "evacuation_success": True,
            "message": "Evacuated " + str(serializer.data.get(
                "units")) + " units from planet Tatooine using starship Millennium Falcon."
        }

        return Response(data)


class StarshipsView(APIView):
    lookup_url_kwarg = "starship_id"

    def get(self, request, **kwargs):
        swapi_service = SwapiService()

        starship_id = self.kwargs.get(self.lookup_url_kwarg)

        species = swapi_service.get_species_by_starship_id(starship_id)

        data = {
            "success": True,
            "species": species
        }

        return Response(data)

    def post(self, request, **kwargs):
        req_data = request.data

        # planet_id = req_data.get("planet_id")
        # starship_id = req_data.get("starship_id")
        #
        # if not isinstance(planet_id, int) or not isinstance(starship_id, int):
        #     return Response("Bad request")

        Starship.objects.create(**req_data)

        data = {
            "success": True,
            "message": "New Starship created successfully."
        }

        return Response(data)


class StarshipSpeciesView(APIView):
    lookup_url_kwarg = "starship_id"

    def get(self, request, **kwargs):
        swapi_service = SwapiService()

        starship_id = self.kwargs.get(self.lookup_url_kwarg)

        species = swapi_service.get_species_by_starship_id(starship_id)

        data = {
            "success": True,
            "species": species
        }

        return Response(data)

    def post(self, request, **kwargs):
        '''
        {
          "name": "New Starship",
          "model": "Model XYZ",
          "manufacturer": "ABC Corp",
          "starship_class": "Transport",
          "crew_capacity": 50
        }
       :param request:
        :param kwargs:
        :return:
        '''
        req_data = request.data
        # planet_id = req_data.get("planet_id")
        # starship_id = req_data.get("starship_id")

        # if not isinstance(planet_id, int) or not isinstance(starship_id, int):
        #     return Response("Bad request")

        # StartShip.objects.create(**req_data)

        data = {
            "success": True,
            "message": "New Starship created successfully."
        }

        return Response(data)


class CreatorSpeciesView(APIView):
    lookup_url_kwarg = "creator_name"

    def get(self, request, **kwargs):
        swapi_service = SwapiService()

        creator_name = self.kwargs.get(self.lookup_url_kwarg)

        species = swapi_service.get_species_by_creator_name(creator_name)

        data = {
            "success": True,
            "species": species
        }

        return Response(data)

    def post(self, request, **kwargs):
        '''
        {
          "name": "New Starship",
          "model": "Model XYZ",
          "manufacturer": "ABC Corp",
          "starship_class": "Transport",
          "crew_capacity": 50
        }
       :param request:
        :param kwargs:
        :return:
        '''
        req_data = request.data
        # planet_id = req_data.get("planet_id")
        # starship_id = req_data.get("starship_id")

        # if not isinstance(planet_id, int) or not isinstance(starship_id, int):
        #     return Response("Bad request")

        # StartShip.objects.create(**req_data)

        data = {
            "success": True,
            "message": "New Starship created successfully."
        }

        return Response(data)
