from utils.httpUtils import http_get


class SwapiHelper:
    def __init__(self):
        self.base_api_url = "https://swapi.dev/api/"

    def getStarShipDetail(self, starship_id):
        pass

    def get_starship_by_Id(self, starship_id):
        return http_get(self.base_api_url + "starships/" + starship_id + "/?format=json")

    def get_film_by_url(self, film_url):
        return http_get(film_url)
        # return http_get(film_url + "/?format=json")

    def get_species_by_url(self, species_url):
        return http_get(species_url)

    def get_all_films(self):
        return http_get(self.base_api_url + "films/?format=json")

    def get_planet_by_id(self, planet_id):
        return http_get(self.base_api_url + "planets/" + planet_id + "/?format=json")

    def search_planet_by_name(self, planet_name):
        return http_get(self.base_api_url + "planets/?name=" + planet_name + "/?format=json")
