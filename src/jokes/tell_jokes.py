from urllib import request
import json
import requests
import pyttsx3

number_of_jokes_from_api = 10


class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"{self.setup} - {self.punchline}"


def make_request_1() -> list:
    response = request.urlopen(
        "https://official-joke-api.appspot.com/random_ten")
    data = response.read()
    json_data = json.loads(data)
    jokes_list = create_jokes_list(json_data)
    return jokes_list


def make_request_2() -> list:
    response = requests.get("https://official-joke-api.appspot.com/random_ten")
    jokes_list = create_jokes_list(response.json())
    return jokes_list


def create_jokes_list(json_data) -> list:
    jokes_list = []
    for item in json_data:
        newJoke = Joke(item["setup"], item["punchline"])
        jokes_list.append(newJoke)

    return jokes_list


def tell() -> None:
    jokes_2 = make_request_2()
    print(f"Got {len(jokes_2)} jokes")

    for joke in jokes_2:
        print(joke)
        pyttsx3.speak(joke.setup)
        pyttsx3.speak(joke.punchline)
