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


dico_armes = {
    "Sploosh-o-matic" : "<:sploosh:1010480744860221440>",
    "Splattershot Jr." : "<:jr:1010480455935606835>",
    "Splash-o-matic" : "<:splash:1010480508263739442>",
    "Splattershot" : "<:splattershot:1010480502341378078>",
    ".52 Gal" : "<:52:1010480347051470889>",
    "N-ZAP '85" : "<:zap:1010480527041626212>",
    "Splattershot Pro" : "<:pro:1010480489150283797>",
    ".96 Gal" : "<:96:1010480370225000488>",
    "Jet Squelcher" : "<:vjs:1010480520624349246>",
    "Luna Blaster" : "<:luna:1010480475581718559>",
    "Blaster" : "<:blaster:1010480387379703879>",
    "Range Blaster" : "<:rb:1010480513833783296>",
    "Clash Blaster" : "<:clash:1010480411757002752>",
    "Rapid Blaster" : "<:rapid:1010480495102005281>",
    "Rapid Blaster Pro" : "<:rapid_pro:1010480546431897680>",
    "L-3 Nozzlenose" : "<:l3:1010480468896002049>",
    "H-3 Nozzlenose" : "<:h3:1010480445378543687>",
    "Squeezer" : "<:squeezer:1010480536365576272>",
    "Carbon Roller" : "<:carbon:1010480104100606002>",
    "Splat Roller" : "<:roller:1010480240310628372>",
    "Dynamo Roller" : "<:dynamo:1010480141153095731>",
    "Flingza Roller" : "<:flingza:1010480170009890837>",
    "Inkbrush" : "<:brush:1010480211462201374>",
    "Octobrush" : "<:octobrush:1010480271633694760>",
    "Classic Squiffer" : "<:squiffer:1010479578654978119>",
    "Splat Charger" : "<:charger:1010479663367331871>",
    "Splatterscope" : "<:scope:1010479699861970984>",
    "E-liter 4K" : "<:eliter:1010479738592165959>",
    "E-liter 4K Scope" : "<:scope_e:1010479773698498610>",
    "Bamboozler 14 Mk I" : "<:bamboo:1010479551522033674>",
    "Goo Tuber" : "<:gootuber:1010479619562029076>",
    "Slosher" : "<:slosher:1010480833368428594>",
    "Tri-Slosher" : "<:tri:1010480890545193072>",
    "Sloshing Machine" : "<:machine:1010480865450676305>",
    "Bloblobber" : "<:blob:1010480782315372564>",
    "Explosher" : "<:explo:1010480807955152917>",
    "Mini Splatling" : "<:mini:1010480997260865678>",
    "Heavy Splatling" : "<:heavy:1010481066408149025>",
    "Hydra Splatling" : "<:hydra:1010480972552228884>",
    "Ballpoint Splatling" : "<:bp:1010480947373817876>",
    "Nautilus 47" : "<:naut:1010481030689472532>",
    "Dapple Dualies" : "<:dapple:1010479913746309130>",
    "Splat Dualies" : "<:dualies:1010479952006750240>",
    "Glooga Dualies" : "<:glooga:1010480064770605087>",
    "Dualie Squelchers" : "<:vds:1010479983501791252>",
    "Dark Tetra Dualies" : "<:tetra:1010480021611221042>",
    "Splat Brella" : "<:brella:1010479399881150474>",
    "Tenta Brella" : "<:tent:1010479510581411880>",
    "Undercover Brella" : "<:under:1010479455338242069>",
    "Random" : "<:uk:1009071227043852310>",

}


list_mode = ["regular", "gachi", "league"]

url = "https://splatoon2.ink/data/schedules.json"
url_salmon = "https://splatoon2.ink/data/coop-schedules.json"

response = requests.get(url=url)
response_salmon = requests.get(url=url_salmon)

all_data = json.loads(response.text)
data_salmon = json.loads(response_salmon.text)



class Salmon:
    def __init__(self, data) -> None:
        self.current_map = data["details"][0]["stage"]["name"]
        self.current_start_time = time.ctime(int(data["schedules"][0]["start_time"]))
        self.current_end_time = time.ctime(int(data["schedules"][0]["end_time"]))

        current_weapon_list = []
        if "coop_special_weapon" in data["details"][0]["weapons"][0]:
            for elt in data["details"][0]["weapons"]:
                current_weapon_list.append(elt["coop_special_weapon"]["name"])

        else :
            for elt in data["details"][0]["weapons"]:
                current_weapon_list.append(elt["weapon"]["name"])

        self.current_weapon_list = f"{dico_armes[current_weapon_list[0]]}  |  {dico_armes[current_weapon_list[1]]} \n{dico_armes[current_weapon_list[2]]}  |  {dico_armes[current_weapon_list[3]]} "


        self.next_map = data["details"][0]["stage"]["name"]
        self.next_start_time = time.ctime(int(data["schedules"][0]["start_time"]))
        self.next_end_time = time.ctime(int(data["schedules"][0]["end_time"]))

        next_weapon_list = []
        if "coop_special_weapon" in data["details"][1]["weapons"][0]:
            for elt in data["details"][1]["weapons"]:
                next_weapon_list.append(elt["coop_special_weapon"]["name"])

        else :
            for elt in data["details"][1]["weapons"]:
                next_weapon_list.append(elt["weapon"]["name"])
        
        self.next_weapon_list = f"{dico_armes[next_weapon_list[0]]}  |  {dico_armes[next_weapon_list[1]]} \n{dico_armes[next_weapon_list[2]]}  |  {dico_armes[next_weapon_list[3]]} "
    

    def __str__(self) -> str:
        return f"Current Rotation : \nMaps : {self.current_map} \n{self.current_weapon_list} \n{self.current_start_time} to {self.current_end_time} \n\nNext Rotation : \nMaps : {self.next_map} \n{self.next_weapon_list}\n{self.next_start_time} {self.next_end_time}"


def get_salmon(data=data_salmon):
    salmon_data = Salmon(data=data_salmon)
    return salmon_data
