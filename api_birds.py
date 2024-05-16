import requests


endpoint = 'https://aves.ninjas.cl/api/birds'

def get_birds():

    response = requests.get(endpoint)

    if response.ok:
        birds = response.json()

    return birds

if __name__ == "__main__":
    print(get_birds())

