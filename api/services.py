from api.helpers import SwapiHelper


class SwapiService:
    def __init__(self):
        self.swapiHelper = SwapiHelper()

    def get_species_by_starship_id(self, starship_id):
        starship = self.get_starship_by_id(starship_id)

        species_urls = []

        for film_url in starship.get("films"):
            film = self.swapiHelper.get_film_by_url(film_url)

            species_urls.extend(film.get("species"))

        return self.get_species_by_urls(species_urls)

    def get_species_by_creator_name(self, creator_name):
        films = self.swapiHelper.get_all_films()

        species_urls = []

        for film in films.get("results"):
            if film.get("producer").find(creator_name) != -1:
                species_urls.extend(film.get("species"))

        return self.get_species_by_urls(species_urls)

    def get_species_by_urls(self, species_urls):
        species_list = []
        species_urls = list(set(species_urls))

        for species_url in species_urls:
            species = self.swapiHelper.get_species_by_url(species_url)
            species_list.append(species.get("name"))

        return list(set(species_list))

    def get_starship_by_id(self, starship_id):
        starship = self.swapiHelper.get_starship_by_Id(starship_id)

        return starship

    def get_evacuation_details(self, starship_id, planet_id_or_name):
        starship = self.get_starship_by_id(starship_id)

        if isinstance(planet_id_or_name, int) or planet_id_or_name.isdigit():
            planet = self.get_planet_by_id(planet_id_or_name)
        else:
            planet = self.get_planet_by_name(planet_id_or_name)

        return {
            "evacuation_units": self.calculate_evacuation_units(starship, planet),
            "starship_name": starship.get("name"),
            "planet_name": planet.get("name"),
        }

    def get_planet_by_id(self, planet_id):
        planet = self.swapiHelper.get_planet_by_id(planet_id)

        return planet

    def calculate_evacuation_units(self, starship, planet):
        units_needed = planet.get("population") if planet.get("population") < starship.get(
            "cargo_capacity") else starship.get("cargo_capacity")

        return units_needed

    def get_planet_by_name(self, planet_name):
        planets = self.swapiHelper.search_planet_by_name(planet_name)

        planet = None

        for each_planet in planets.get("results"):
            if each_planet.get("name").find(planet_name) != -1:
                planet = each_planet

        return planet
