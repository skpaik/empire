import requests


def http_get(url):
    res = requests.get(url)
    print(url + " : " + str(res.status_code))
    return res.json()


def http_pot(url, data):
    res = requests.post(url, json=data)
    print(url + " : " + str(res.status_code))
    return res.json()
