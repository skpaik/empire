import requests


def test_starships_create():
    url = "http://localhost:8000/api/starships/"
    data = {
        "name": "New Starship",
        "model": "Model XYZ",
        "manufacturer": "ABC Corp",
        "starship_class": "Transport",
        "crew_capacity": 50
    }

    response = requests.post(url, data=data)
    assert response.status_code == 200


def test_get_species_by_creator_name():
    url = ("http://localhost:8000/api/starship/creator/{creator_name}/species"
           .format(creator_name="Gary Kurtz"))

    response = requests.get(url)

    assert response.status_code == 200


def test_get_species_by_starship_id_and_creator_name():
    url = ("http://localhost:8000/api/species?starship_id={starship_id}&creator={creator}"
           .format(starship_id=9, creator="Rick McCallum"))

    response = requests.get(url)

    assert response.status_code == 200


def test_get_species_by_starship_id():
    url = ("http://localhost:8000/api/starship/{starship_id}/species/"
           .format(starship_id=3))

    response = requests.get(url)

    assert response.status_code == 200


def test_get_evacuate_units_by_name():
    url = ("http://localhost:8000/api/evacuate/{starship_id}/planet/{planet_id_or_name}"
           .format(starship_id=3, planet_id_or_name="Yavin IV"))

    response = requests.get(url)

    assert response.status_code == 200


def test_get_evacuate_units_by_id():
    url = ("http://localhost:8000/api/evacuate/{starship_id}/planet/{planet_id_or_name}"
           .format(starship_id=3, planet_id_or_name=2))

    response = requests.get(url)

    assert response.status_code == 200
