import logging
import os
import json
from honkaiDex.base.stigamata import StigamataSet

HONKAIDEX_DATA = os.path.dirname(os.path.realpath(__file__))

HONKAI_FANDOM = "https://honkaiimpact3.fandom.com"
HONKAI_FANDOM_STIGAMATA = "https://honkaiimpact3.fandom.com/wiki/Stigmata"

def load_stigamata_1():
    logging.debug("Loading stigamata_1.json")

    json_data = {}

    with open(os.path.join(HONKAIDEX_DATA, "stigamata_1.json"), "r") as f:
        json_data = json.load(f)

    for item in json_data:
        StigamataSet.create(
            name=item["name"],
            top=item["top_e"],
            mid=item["mid_e"],
            bot=item["bot_e"],
            two_piece=item["two_piece"],
            three_piece=item["three_piece"],
            obtainable=item["obtainable"],
        )
    