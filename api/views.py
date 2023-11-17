import json

from rest_framework.views import *

from api.models import XWing2


class SpeciesView(APIView):
    # Does something to get xwings
    def get(self, request, **kwargs):
        data = {
            "starship_id": 9,
            "creator": "George Lucas",
            "species": ["Human", "Wookiee", "Rodian"]
        }
        return Response(data)

    def post(self, request, **kwargs):
        id = request.data.get("id")
        if not isinstance(id, int):
            return Response("Bad request")
        XWing2.objects.create(**request.data)
        return Response("ok")


class DefenceTowerView(APIView):
    # TODO: I want to be able to get all towers targeting given xwing
    # TODO: As a pilot of XWing I want to be able to destroy the tower if it's targeting me
    pass
