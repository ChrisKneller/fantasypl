import requests
import json
from pprint import pprint
from time import struct_time, gmtime, strftime

'''
List of all known API urls


https://fantasy.premierleague.com/api/entry/{player_id}/
https://fantasy.premierleague.com/api/entry/{player_id}/history/
https://fantasy.premierleague.com/api/fixtures/
https://fantasy.premierleague.com/api/fixtures/?event={gameweek}
https://fantasy.premierleague.com/api/leagues-classic/{classic_league_id}/standings/?page_new_entries={page}&page_standings={GAMEWEEK? #TODO: FIND OUT WHAT THIS IS}
https://fantasy.premierleague.com/api/bootstrap-static/

Login required:
https://fantasy.premierleague.com/api/my-team/{player_id}/
https://fantasy.premierleague.com/api/me/


'''

base_url = 'https://fantasy.premierleague.com/api'


# input player id (e.g. 68762); output player details
def get_player_details(player_id):
    r = requests.get(f'{base_url}/entry/{player_id}/')
    webdata = json.loads(r.text)
    # webdata = pprint(webdata)
    return webdata


# input league id; output league details


# get all details
# dict_keys(['events', 'game_settings', 'phases', 'teams', 'total_players', 'elements', 'element_stats', 'element_types'])
def get_all_details():
    r = requests.get(f'{base_url}/bootstrap-static/')
    webdata = json.loads(r.text)
    return webdata


# get all gameweek details
def get_all_gameweek_details():
    return get_all_details()['events']


# input gameweek number; output details of that gameweek
def get_gameweek_details(gameweek_number):
    return get_all_gameweek_details()[gameweek_number-1]


# get all team details
def get_all_team_details():
    return get_all_details()['teams']


class Player():
    # a Player object based on the Player's id

    def __init__(self, id):

        self.id = id
        self.data = get_player_details(id)
        self.first_name = self.data['player_first_name']
        self.last_name = self.data['player_last_name']
        self.team_name = self.data['name']
        self.region = self.data['player_region_name']
        self.gw_points = self.data['summary_event_points']
        self.gw_rank = self.data['summary_event_rank']
        self.total_points = self.data['summary_overall_points']
        self.total_rank = self.data['summary_overall_rank']

    # return a list of classic league ids that the Player is a part of
    def classic_leagues(self):
        classic_leagues = []
        leagues_data = self.data['leagues']['classic']
        for league in leagues_data:
            classic_leagues.append(league['id'])
        return classic_leagues

    # return a list of h2h league ids that the Player is a part of
    def h2h_leagues(self):
        h2h_leagues = []
        leagues_data = self.data['leagues']['h2h']
        for league in leagues_data:
            h2h_leagues.append(league['id'])
        return h2h_leagues

# TODO: define League class properly

class League():
    # a League object based on the League's id

    def __init__(self, id):

        self.id = id

# TODO: expand definition of class
class Gameweek():
    # a Gameweek object containing data for each gameweek

    def __init__(self, gameweek_number):

        self.number = gameweek_number
        self.data = get_gameweek_details(gameweek_number)
        self.deadline = self.data['deadline_time']
        self.deadline_epoch = self.data['deadline_time_epoch']
        self.deadline_verbose = strftime('%H:%M %Z on %A %d %B %Y',gmtime(self.data['deadline_time_epoch']))

# TODO: define some other classes ?!