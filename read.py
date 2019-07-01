import requests
import json
from pprint import pprint

base_url = 'https://fantasy.premierleague.com/api'


# input league number; output league details (e.g. 68762)
def get_player_details(player_id):
    r = requests.get(f'{base_url}/entry/{player_id}/')
    webdata = json.loads(r.text)
    # webdata = pprint(webdata)
    return webdata


class Player():
    # a player object based on the player's id
    
    def __init__(self, id):

        self.id = id
        self.data = get_player_details(68762)
        self.first_name = self.data['player_first_name']
        self.last_name = self.data['player_last_name']
        self.team_name = self.data['name']
        self.leagues = [] # TODO: LOOP OVER LEAGUES AND GET LIST
            # leagues = leagues.data['leagues']
            # classic_leagues = leagues['classic']
            # h2h_leagues = leagues['h2h']
        self.region = self.data['player_region_name']
        self.gw_points = self.data['summary_event_points']
        self.gw_rank = self.data['summary_event_rank']
        self.total_points = self.data['summary_overall_points']
        self.total_rank = self.data['summary_overall_rank']
    

# TODO: define League class and use it in above self.leagues definition