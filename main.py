import json
import requests

from splatnet.splatnet2.config import Config
from splatnet.splatnet2.models import Result, Results, Player

import time

from discord import *
import discord.ui as bt
from discord.ext import commands


client = Client()

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description="Bot de clem#1777", intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
    print("Ready !")
    activity = Game(name="!help", type=1)
    await bot.change_presence(status=Status.online, activity=activity)

@bot.command()
async def last(ctx, number=0):
    config = Config("../token/config.json")
    splatnet = Splatnet2(config)
    results = splatnet.results()
    ilisible = splatnet.result(results.results[int(number)].battle_number)
    my_team, ennemy_team, game_stats = splatnet.get_results(ilisible)

    res_my_team = ""
    for mess in my_team:
        res_my_team = res_my_team + mess
    embed_my_team = Embed(title="My Team", description=res_my_team, color=0x33CAFF)

    res_ennemy = ""
    for mess in ennemy_team:
        res_ennemy = res_ennemy + mess
    embed_ennemy = Embed(title="Ennemy Team", description=res_ennemy, color=0x33CAFF)

    embed_game = Embed(title="Game Infos", description=game_stats, color=0x33CAFF)
    await ctx.send(embed=embed_my_team)
    await ctx.send(embed=embed_ennemy)
    await ctx.send(embed=embed_game)

@bot.command()
async def stats(ctx, number):
    await last(ctx, number)

dico_stuff = {
    "Main Power Up" : "<:mpu:1009070739170799626>",
    "Ability Doubler" : "<:ab:1009070271661084733>",
    "Run Speed Up" : "<:rsu:1009070594911907901>",
    "Swim Speed Up" : "<:ssu:1009071046105759865>",
    "Ink Saver (Main)" : "<:ism:1009070712822181901>",
    "Ink Saver (Sub)" : "<:iss:1009071116842717275>",
    "Special Saver" : "<:ss:1009070872616763463>",
    "Special Charge Up" : "<:scu:1009070989474271322>",
    "Quick Respawn" : "<:qr:1009070895383466046>",
    "Quick Super Jump" : "<:qsj:1009070688256151624>",
    "Comeback" : "<:cbk:1009070396429062195>",
    "Ink Resistance Up" : "<:ir:1009070848931532881>",
    "Bomb Defense Up DX" : "<:bdu:1009070315814518816>",
    "Respawn Punisher" : "<:rsp:1009070563580452914>",
    "question mark" : "<:uk:1009071227043852310>",
    "uk" : "<:uk:1009071227043852310>",
    "Stealth Jump" : "<:sj:1009071141664604200>",
    "Special Power Up" : "<:spu:1009071008021483530>",
    "Ink Recovery Up" : "<:iru:1009070659843919913>",
    "Object Shredder" : "<:os:1009070825023995996>",
    "Last-Ditch Effort" : "<:lde:1009070541711343756>",
    "Ninja Squid" : "<:ns:1009071068360753242>",
    "Drop Roller" : "<:dr:1009070967785525299>",
    "Thermal Ink" : "<:ti:1009071170018095126>",
    "Tenacity" : "<:tnty:1009070763745234944>",
    "Opening Gambit" : "<:og:1009071094352838727>",
    "Haunt" : "<:hnt:1009070429064941628>",
    "Sub Power Up" : "<:sbpu:1009070353810735196>",
}

dico_spe = {
    "Tenta Missiles" : "<:missiles:1009101166732378232>",
    "Sting Ray" : "<:sting:1009101111526965269>",
    "Inkjet" : "<:inkjet:1009101175435563020>",
    "Splashdown" : "<:splashdown:1009101152434004070>",
    "Ink Armor" : "<:armor:1009101295170359327>",
    "Autobomb Laucher" : "<:autobomb:1009101223598764032>",
    "Burst-Bomb Laucher" : "<:burst:1009101252287811594> ",
    "Curling-Bomb Launcher" : "<:curling:1009101190925144105>",
    "Splat-Bomb Launcher" : "<:splat:1009101120955760740>",
    "Suction-Bomb Laucher" : "<:suction:1009101054207594556>",
    "Ink Storm" : "<:storm:1009101099489312860>",
    "Baller" : "<:baller:1009101289390604298>",
    "Bubble Blower" : "<:bubble:1009101278124711986>",
    "Booyah Bomb" : "<:booyah:1009101284055457913>",
    "Ultra Stamp" : "<:stamp:1009100969948229682>",
}

class Splatnet2:
    config: Config

    def __init__(self, config: Config):
        self.config = config
        self.path = "/api/results"
        self.response = None

    def results(self) -> Results:
        data = self._call("/api/results")
        return Results(**data)

    def result(self, battle_number: str) -> Result:
        data = self._call(f"/api/results/{battle_number}")
        return Result(**data)

    def _call(self, path: str) -> dict:
        headers = {
            "x-unique-id": "32449507786579989234",
            "x-requested-with": "XMLHttpRequest",
            "x-timezone-offset": self.config.timezone_offset(),
            "Accept-Language": self.config.language(),
            "Cookie": f"iksm_session={self.config.iksm_session()}",
        }
        self.response = requests.get(
            f"https://app.splatoon2.nintendo.net{path}", headers=headers
        )

        return json.loads(self.response.text)



    def get_stuff(self, player):
        stuff = dico_stuff[player.player.head_skills.main.name] + " | "
        for sub_name in player.player.head_skills.subs:
            if sub_name == None:
                stuff = stuff + dico_stuff["uk"]
            else:
                stuff = stuff + dico_stuff[sub_name.name]
        
        stuff = stuff + f"\n{dico_stuff[player.player.clothes_skills.main.name]} | "
        for sub_name in player.player.clothes_skills.subs:
            if sub_name == None:
                stuff = stuff + dico_stuff["uk"]
            else:
                stuff = stuff + dico_stuff[sub_name.name]
        
        stuff = stuff + f"\n{dico_stuff[player.player.shoes_skills.main.name]} | "
        for sub_name in player.player.shoes_skills.subs:
            if sub_name == None:
                stuff = stuff + dico_stuff["uk"]
            else:
                stuff = stuff + dico_stuff[sub_name.name]

        return stuff


    def get_results(self, result:Result):

        my_team = []
        ennemy_team = []

        player = (result.player_result)
        stuff = self.get_stuff(player)
        spe = dico_spe[player.player.weapon.special.name]
        message_bien = (f"name : {player.player.nickname} , {player.game_paint_point} turf points , rank :{player.player.player_rank}, {player.player.star_rank}* \nweapon used : {player.player.weapon.name} \nkills {player.kill_count} ; assists {player.assist_count} ; deaths {player.death_count} ; specials {spe} {player.special_count}\n{stuff} \n\n")
        my_team.append(message_bien)

        for player in result.my_team_members:
            stuff = self.get_stuff(player)
            spe = dico_spe[player.player.weapon.special.name]
            message_bien = (f"name : {player.player.nickname} , {player.game_paint_point} turf points , rank :{player.player.player_rank}, {player.player.star_rank}* \nweapon used : {player.player.weapon.name} \nkills {player.kill_count} ; assists {player.assist_count} ; deaths {player.death_count} ; specials {spe} {player.special_count}\n{stuff} \n\n")
            my_team.append(message_bien)

        for player in result.other_team_members:
            stuff = self.get_stuff(player)
            spe = dico_spe[player.player.weapon.special.name]
            a = ((f"name : {player.player.nickname} , {player.game_paint_point} turf points , rank :{player.player.player_rank}, {player.player.star_rank}* \nweapon used : {player.player.weapon.name} \nkills {player.kill_count} ; assists {player.assist_count} ; deaths {player.death_count} ; specials {spe} {player.special_count}\n{stuff} \n\n"))
            ennemy_team.append(a)
            
        if result.game_mode.name == "Ranked Battle":
            if result.my_team_count > result.other_team_count:
                win_state = "won"
            else:
                win_state = "lost"

            duree = str(result.elapsed_time/60).replace(".",":")
            score = f"Score : player's team {result.my_team_count} | {result.other_team_count} ennemy team\nroom power : {result.estimate_x_power} | your X power : {result.x_power} "
        
        elif result.game_mode.name == "Turf War":
            if result.my_team_percentage > result.other_team_percentage:
                win_state="won"
            else:
                win_state = "lost"
            duree = "3:00"
            score = f"Score : player's team {result.my_team_percentage}% | {result.other_team_percentage}% ennemy team"
        
        elif result.game_mode.name == "Private Battle":
            if result.type == "gachi":
                if result.my_team_count > result.other_team_count:
                    win_state = "won"
                else:
                    win_state = "lost"

                duree = str(result.elapsed_time/60).replace(".",":")
                score = f"Score : player's team {result.my_team_count} | {result.other_team_count} ennemy team\nroom power : {result.estimate_x_power} | your X power : {result.x_power} "
            
            elif result.type == "regular":
                if result.my_team_percentage > result.other_team_percentage:
                    win_state="won"
                else:
                    win_state = "lost"
                duree = "3:00"
                score = f"Score : player's team {result.my_team_percentage}% | {result.other_team_percentage}% ennemy team"

        game_stats = (f"your team {win_state} on {result.stage.name} ({result.game_mode.name} mode : {result.rule.name})\n{score} \nmatch date {time.ctime(result.start_time)} ({duree[:4]} minutes)" )

        return my_team, ennemy_team, game_stats


import sys

try:
    sys.path.append("/python/token")
    import token_bot
except:
    sys.path.append("/home/cleeem/python/token")
    import token_bot
    
token_run = token_bot.tokens["token_bot_splatnet"]

bot.run(token_run)
