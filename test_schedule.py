import json
import time
import requests


class Rotation:
    def __init__(self, data) -> None:
        self.type = data[0]["game_mode"]["name"]

        current_stage_a = data[0]["stage_a"]["name"]
        current_stage_b = data[0]["stage_b"]["name"]
        self.current_maps = f"{current_stage_a} \n{current_stage_b}"
        self.current_mode = data[0]["rule"]["name"] + " " + dico_emote[data[0]["rule"]["name"]]
        self.current_start_time = time.ctime(int(data[0]["start_time"]))
        self.current_end_time = time.ctime(int(data[0]["end_time"]))

        next_stage_a = data[1]["stage_a"]["name"]
        next_stage_b = data[1]["stage_b"]["name"]
        self.next_maps = f"{next_stage_a} \n{next_stage_b}"
        self.next_mode = data[1]["rule"]["name"] + " " + dico_emote[data[1]["rule"]["name"]]
        self.next_start_time = time.ctime(int(data[1]["start_time"]))
        self.next_end_time = time.ctime(int(data[1]["end_time"]))

    def __str__(self) -> str:
        return f"Current Rotation : \nMaps : {self.current_maps} \nMode : {self.current_mode}\n{self.current_start_time} to {self.current_end_time} \n\nNext Rotation : \nMaps : {self.next_maps} \nMode : {self.next_mode}\n{self.next_start_time} {self.next_end_time}"


def get_data(data:list):
    rotation_data = Rotation(data=data)
    return rotation_data

dico_emote = {
    "Clam Blitz" : "<:cb:853656449825243166>",
    "Rainmaker" : "<:rm:853656465725456424>",
    "Tower Control" : "<:tc:853656463846146068>",
    "Splat Zones" : "<:sz:853656465423990807>",
    "Turf War" : "<:turf:1010462680663994418>"
}

url = "https://splatoon2.ink/data/schedules.json"
response = requests.get(url=url)
all_data = json.loads(response.text)


list_mode = ["regular", "gachi", "league"]