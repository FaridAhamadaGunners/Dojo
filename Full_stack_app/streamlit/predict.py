import requests


def process(list_reponses: dict, server_url: str):
    pred = requests.post(server_url,
                         json={"Favorite Color": list_reponses["Favorite Color"],
                               "Favorite Music Genre": list_reponses["Favorite Music Genre"],
                               "Favorite Beverage": list_reponses["Favorite Beverage"],
                               "Favorite Soft Drink": list_reponses["Favorite Soft Drink"]})
    return pred.text
