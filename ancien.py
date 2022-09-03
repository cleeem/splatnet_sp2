class Splatnet2:
    def __init__(self) -> None:
        pass
#     config: Config

#     def __init__(self, config: Config):
#         self.config = config
#         self.path = "/api/results"
#         self.response = None

#     def results(self) -> Results:
#         data = self._call("/api/results")
#         return Results(**data)

#     def result(self, battle_number: str) -> Result:
#         data = self._call(f"/api/results/{battle_number}")
#         return Result(**data)

#     def _call(self, path: str) -> dict:
#         headers = {
#             "x-unique-id": "32449507786579989234",
#             "x-requested-with": "XMLHttpRequest",
#             "x-timezone-offset": self.config.timezone_offset(),
#             "Accept-Language": self.config.language(),
#             "Cookie": f"iksm_session={self.config.iksm_session()}",
#         }
#         self.response = requests.get(
#             f"https://app.splatoon2.nintendo.net{path}", headers=headers
#         )

#         return json.loads(self.response.text)

#     def get_stuff(self, player):
#         stuff = dico_stuff[player.player.head_skills.main.name] + " | "
#         for sub_name in player.player.head_skills.subs:
#             if sub_name == None:
#                 stuff = stuff + dico_stuff["uk"]
#             else:
#                 stuff = stuff + dico_stuff[sub_name.name]
        
#         stuff = stuff + f"\n{dico_stuff[player.player.clothes_skills.main.name]} | "
#         for sub_name in player.player.clothes_skills.subs:
#             if sub_name == None:
#                 stuff = stuff + dico_stuff["uk"]
#             else:
#                 stuff = stuff + dico_stuff[sub_name.name]
        
#         stuff = stuff + f"\n{dico_stuff[player.player.shoes_skills.main.name]} | "
#         for sub_name in player.player.shoes_skills.subs:
#             if sub_name == None:
#                 stuff = stuff + dico_stuff["uk"]
#             else:
#                 stuff = stuff + dico_stuff[sub_name.name]

#         return stuff

#     def get_results(self, result:Result):

#         my_team = []
#         ennemy_team = []

#         player = (result.player_result)
#         stuff = self.get_stuff(player)
#         spe = dico_spe[player.player.weapon.special.name]
#         message_bien = (f"name : {player.player.nickname} , {player.game_paint_point} turf points , rank :{player.player.player_rank}, {player.player.star_rank}* \nweapon used : {player.player.weapon.name} \nkills {player.kill_count} ; assists {player.assist_count} ; deaths {player.death_count} ; specials {spe} {player.special_count}\n{stuff} \n\n")
#         my_team.append(message_bien)

#         for player in result.my_team_members:
#             stuff = self.get_stuff(player)
#             spe = dico_spe[player.player.weapon.special.name]
#             message_bien = (f"name : {player.player.nickname} , {player.game_paint_point} turf points , rank :{player.player.player_rank}, {player.player.star_rank}* \nweapon used : {player.player.weapon.name} \nkills {player.kill_count} ; assists {player.assist_count} ; deaths {player.death_count} ; specials {spe} {player.special_count}\n{stuff} \n\n")
#             my_team.append(message_bien)

#         for player in result.other_team_members:
#             stuff = self.get_stuff(player)
#             spe = dico_spe[player.player.weapon.special.name]
#             a = ((f"name : {player.player.nickname} , {player.game_paint_point} turf points , rank :{player.player.player_rank}, {player.player.star_rank}* \nweapon used : {player.player.weapon.name} \nkills {player.kill_count} ; assists {player.assist_count} ; deaths {player.death_count} ; specials {spe} {player.special_count}\n{stuff} \n\n"))
#             ennemy_team.append(a)
            
#         if result.game_mode.name == "Ranked Battle":
#             if result.my_team_count > result.other_team_count:
#                 win_state = "won"
#             else:
#                 win_state = "lost"

#             duree = str(result.elapsed_time/60).replace(".",":")
#             score = f"Score : player's team {result.my_team_count} | {result.other_team_count} ennemy team\nroom power : {result.estimate_x_power} | your X power : {result.x_power} "
        
#         elif result.game_mode.name == "Turf War":
#             if result.my_team_percentage > result.other_team_percentage:
#                 win_state="won"
#             else:
#                 win_state = "lost"
#             duree = "3:00"
#             score = f"Score : player's team {result.my_team_percentage}% | {result.other_team_percentage}% ennemy team"
        
#         elif result.game_mode.name == "Private Battle":
#             if result.type == "gachi":
#                 if result.my_team_count > result.other_team_count:
#                     win_state = "won"
#                 else:
#                     win_state = "lost"

#                 duree = str(result.elapsed_time/60).replace(".",":")
#                 score = f"Score : player's team {result.my_team_count} | {result.other_team_count} ennemy team\nroom power : {result.estimate_x_power} | your X power : {result.x_power} "
            
#             elif result.type == "regular":
#                 if result.my_team_percentage > result.other_team_percentage:
#                     win_state="won"
#                 else:
#                     win_state = "lost"
#                 duree = "3:00"
#                 score = f"Score : player's team {result.my_team_percentage}% | {result.other_team_percentage}% ennemy team"

#         if result.game_mode.name == "League Battle":
#             if result.my_team_count > result.other_team_count:
#                 win_state = "won"
#             else:
#                 win_state = "lost"

#             duree = str(result.elapsed_time/60).replace(".",":")
#             score = f"Score : player's team {result.my_team_count} | {result.other_team_count} ennemy team\nroom power : {result.estimate_x_power} | your X power : {result.x_power} "
        

#         game_stats = (f"your team {win_state} on {result.stage.name} ({result.game_mode.name} mode : {result.rule.name})\n{score} \nmatch date {time.ctime(result.start_time)} ({duree[:4]} minutes)" )

#         return my_team, ennemy_team, game_stats

#     def test_splat(self):
#         headers = {
#             "x-unique-id": "32449507786579989234",
#             "x-requested-with": "XMLHttpRequest",
#             "x-timezone-offset": self.config.timezone_offset(),
#             "Accept-Language": self.config.language(),
#             "Cookie": f"iksm_session={self.config.iksm_session()}",
#         }
#         response = requests.get(
#             f"https://app.splatoon2.nintendo.net{self.path}", headers=headers
#         )

#         print(response.text)

    pass