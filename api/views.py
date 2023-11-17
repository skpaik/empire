from rest_framework.views import *

from api.models import Starship
from api.services import SwapiService


class SpeciesView(APIView):
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


class EvacuateView(APIView):
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
