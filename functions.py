import requests
import json
# from classes import Player

# This file is intended to contain all standalone functions that can be
# optionally run without being in a session.

base_url = 'https://fantasy.premierleague.com/api'

# input player id (e.g. 68762); output player details
def get_player_details(player_id, session=None):
    query = f'{base_url}/entry/{player_id}/'
    r = requests.get(query) if not session else session.get(query)
    webdata = json.loads(r.text)
    return Player(webdata)


# TODO: add optional session inputs for the below


# get all details
# dict_keys(['events', 'game_settings', 'phases', 'teams', 'total_players', 'elements' (footballers), 'element_stats', 'element_types'])
def get_all_details(session = None):
    query = f'{base_url}/bootstrap-static/'
    r = requests.get(query) if not session else session.get(query)
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
