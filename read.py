import requests
import json
from pprint import pprint
from time import struct_time, gmtime, strftime

'''
List of all known API urls

* /bootstrap-static/
* /entry/{player_id}/
* /entry/{player_id}/history/
* /fixtures/
* /fixtures/?event={gameweek}
* /element-summary/{player_id}/
* /leagues-classic/{classic_league_id}/standings/?page_new_entries={page}&page_standings={GAMEWEEK? #TODO: FIND OUT WHAT THIS IS}


Login required:
* /my-team/{player_id}/
* /me/

'''

base_url = 'https://fantasy.premierleague.com/api'


# TODO: in order to use any of these functions, create a master Class that begins the session
# and sends all requests in that one session


# input player id (e.g. 68762); output player details
def get_player_details(player_id):
    r = requests.get(f'{base_url}/entry/{player_id}/')
    webdata = json.loads(r.text)
    # webdata = pprint(webdata)
    return webdata


# input league id; output league details


# get all details
# dict_keys(['events', 'game_settings', 'phases', 'teams', 'total_players', 'elements' (footballers), 'element_stats', 'element_types'])
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

# TODO: expand for fixtures
class Gameweek():
    # a Gameweek object containing data for each gameweek

    def __init__(self, gameweek_number):

        self.number = gameweek_number
        self.data = get_gameweek_details(gameweek_number)
        self.deadline = self.data['deadline_time']
        self.deadline_epoch = self.data['deadline_time_epoch']
        self.deadline_verbose = strftime('%H:%M %Z on %A %d %B %Y',gmtime(self.data['deadline_time_epoch']))
        self.is_next = self.data['is_next']
        self.is_current = self.data['is_current']
        self.is_previous = self.data['is_previous']
        self.average_score = self.data['average_entry_score']
        self.highest_score = self.data['highest_score']
        self.highest_scoring_entry = self.data['highest_scoring_entry']
        self.finished = self.data['finished']
        self.data_checked = self.data['data_checked']
        # self.fixtures = 

# TODO: expand class
class Team():
    # a Team object containing data for the corresponding premier league team
    
    def __init__(self, team_number):
        self.id = team_number
        self.name = 'xyz' # TODO


# TODO: expand class
class Footballer():
    # a Footballer object containing data for the corresponding football player

    def __init__(self, id):
        self.id = id
        self.first_name = 'placeholder'