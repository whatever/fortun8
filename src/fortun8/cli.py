import cohere
import os

from collections import namedtuple
from datetime import datetime
from fortun8.prompt_factory import Prompter


def get_cohere_client():

    if "COHERE_API_KEY" not in os.environ:
        raise ValueError("COHERE_API_KEY is not set")

    co = cohere.Client(os.getenv("COHERE_API_KEY"))

    return co


def get_feelings_map():

    feelings = {}

    for hour in range(5):
        feelings[hour] = Vibe("sleepy", "sleepy")

    for hour in range(5, 9):
        feelings[hour] = Vibe("sleepy", "hopeful")

    for hour in range(9, 12):
        feelings[hour] = Vibe("productive", "ambitious")

    for hour in range(12, 14):
        feelings[hour] = Vibe("hungry", "relaxed")

    for hour in range(14, 15):
        feelings[hour] = Vibe("sleepy", "ambitious")

    for hour in range(15, 18):
        feelings[hour] = Vibe("a little tired", "ambitious")

    for hour in range(18, 21):
        feelings[hour] = Vibe("relaxed", "peaceful")

    for hour in range(21, 24):
        feelings[hour] = Vibe("sleepy", "peaceful")

    return feelings


Vibe = namedtuple("Vibe", ["feeling", "whats_next"])


def main():

    feelings = get_feelings_map()

    prompter = Prompter()

    client = get_cohere_client()

    vibe = feelings[datetime.now().hour]

    response = client.generate(
        prompt=prompter.text(feeling=vibe.feeling, whats_next=vibe.whats_next),
        stream=True,
    )

    for r in response:
        print(r.text, end="")

    print()
