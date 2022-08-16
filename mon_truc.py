import json
import requests

from splatnet.splatnet2.config import Config
from splatnet.splatnet2.models import Result, Results

class Stuff:
    def __init__(self) -> None:
        self.head = {}
        self.clothes = {}
        self.shoes = {}

    def __str__(self) -> str:
        return f"{self.head}\n{self.clothes}\n{self.shoes}"

    def set_stuff(self, piece, stuff):
        if "head" in piece:
            self.head[piece] = stuff

        elif "clothes" in piece:
            self.clothes[piece] = stuff
        
        elif "shoes" in piece:
            self.shoes[piece] = stuff

class Player:
    def __init__(self) -> None:
        self.name : str
        self.rank : str
        self.stars : int
        self.weapon : str
        self.weapon_paint : int
        self.turf : int
        self.x_power : str
        self.stuff : Stuff
        self.team_win : str
        self.kills_count : int
        self.death_count : int
        self.assist_count : int
        self.special_count : int

        
    def __str__(self) -> str:
        return f"name : {self.name} , {self.turf} turf points , rank :{self.rank}, {self.stars}* \nkills : {self.kills_count}  assists : {self.assist_count}\ndeaths : {self.death_count}  specials : {self.special_count}\nweapon used : {self.weapon}, overall paint with this wepon : {self.weapon_paint} points\ncurrent X rank power : {self.x_power}\n{self.stuff} "


class Game:
    def __init__(self) -> None:
        self.joueur : Player
        self.map : str
        self.win : str
        self.rank_turf : str
        self.rule : str
        self.room_power : str
        self.top_500 : int
        self.player_team_count : int
        self.ennemy_count : int
        self.start_time : str
        self.duration : str
        
    def __str__(self) -> str:
        return f"{self.joueur.name} won on {self.map} ({self.rank_turf} mode : {self.rule})\nScore : player's team {self.player_team_count} | {self.ennemy_count} ennemy team\nroom power : {self.room_power} number of top 500 : {self.top_500}\nmatch started at {self.start_time} and last for {self.duration}"

class Splatnet2:
    config: Config

    def __init__(self, config: Config):
        self.config = config

    def get_info_sub(self, dico):
        liste_info = []
        liste_info.append(dico["main"]["name"])
        for dico_subs in dico["subs"]:
            liste_info.append(dico_subs["name"])
        return liste_info

    def results(self) -> dict:
        path = "/api/results"
        headers = {
            "x-unique-id": "32449507786579989234",
            "x-requested-with": "XMLHttpRequest",
            "x-timezone-offset": self.config.timezone_offset(),
            "Accept-Language": self.config.language(),
            "Cookie": f"iksm_session={self.config.iksm_session()}",
        }
        response = requests.get(
            f"https://app.splatoon2.nintendo.net{path}", headers=headers
        )
        
       
        dico_response = json.loads(response.text)

        list_results = dico_response["results"]
            
        mid = list_results[0]

        dico_player = list_results[0]["player_result"]

        player = dico_player["player"]

        joueur = Player()

        joueur.name = player["nickname"]
        joueur.weapon = player["weapon"]["name"]
        joueur.weapon_paint = mid["weapon_paint_point"]
        joueur.turf = dico_player["game_paint_point"]
        joueur.kills_count = dico_player["kill_count"]
        joueur.death_count = dico_player["death_count"]
        joueur.assist_count = dico_player["assist_count"]
        joueur.special_count = dico_player["special_count"]
        joueur.rank = mid["player_rank"]
        joueur.stars = mid["star_rank"]
        joueur.x_power = mid["x_power"]

        all_subs_info = None

        stuff = Stuff()
        
        for k,v in player.items():
            if "skills" in k:
                all_subs_info = self.get_info_sub(v)
                stuff.set_stuff(k, all_subs_info)

        joueur.stuff = stuff

        print(joueur)
        print()
        print()

        game = Game()
        game.duration = mid["elapsed_time"]
        game.start_time = mid["start_time"]
        game.player_team_count = mid["my_team_count"]
        game.ennemy_count = mid["other_team_count"]
        game.joueur = joueur
        game.map = mid["stage"]["name"]
        game.rank_turf = mid["game_mode"]["name"]
        game.rule = mid["rule"]["name"]
        game.room_power = mid["estimate_x_power"]
        game.win = mid["my_team_result"]["name"]
        game.top_500 = mid.get("crown_player")
        
        print(game)

if __name__ == "__main__":
    config = Config()
    splatnet = Splatnet2(config)
    splatnet.results()