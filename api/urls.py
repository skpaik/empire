from django.urls import path

from api.views import SpeciesView, EvacuateView, StarshipsView, StarshipSpeciesView, CreatorSpeciesView

urlpatterns = [
    path("species/", SpeciesView.as_view()),
    path("starship/<starship_id>/species/", StarshipSpeciesView.as_view()),
    path("starship/creator/<creator_name>/species/", CreatorSpeciesView.as_view()),
    path("evacuate/<starship_id>/planet/<planet_id_or_name>/", EvacuateView.as_view()),
    path("starships/", StarshipsView.as_view()),
]
