from django.urls import path
from api.views import SpeciesView

urlpatterns = [
    path("species/", SpeciesView.as_view()),
]
