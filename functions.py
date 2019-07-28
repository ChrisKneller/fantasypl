import requests
import json
from .endpoints import API_URLS, API_BASE_URL
# from .classes import ClassicLeague
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


def position_id_to_str(id_no):
    positions = {1: 'Goalkeeper',
                2: 'Defender',
                3: 'Midfielder',
                4: 'Forward'}
    return positions[id_no]


def team_id_to_str(id_no):
    teams = {1: 'Arsenal',
             2: 'Aston Villa',
             3: 'Bournemouth',
             4: 'Brighton',
             5: 'Burnley',
             6: 'Chelsea',
             7: 'Crystal Palace',
             8: 'Everton',
             9: 'Leicester',
             10: 'Liverpool',
             11: 'Man City',
             12: 'Man Utd',
             13: 'Newcastle',
             14: 'Norwich',
             15: 'Sheffield Utd',
             16: 'Southampton',
             17: 'Spurs',
             18: 'Watford',
             19: 'West Ham',
             20: 'Wolves',}
    return teams[id_no]


def get_classicleague(league_id, session=False):
    # Input a classic league ID, output the ClassicLeague class containing its information
    query = API_URLS['league_classic'].format(league_id)
    r = session.get(query) if session else requests.get(query)
    webdata = json.loads(r.text)
    return ClassicLeague(webdata, session)


def fetch(query, session=False, proxies=None):
    r = session.get(query, proxies=proxies) if session else requests.get(query, proxies=proxies)
    webdata = json.loads(r.text)
    return webdata


def post(query, session=False, payload=None, headers=None, proxies=None):
    r = session.post(query, data=payload, headers=headers, proxies=proxies) if session else request.post(query, data=payload, headers=headers, proxies=proxies)
    return response

def get_headers(referer='https://fantasy.premierleague.com/', login=False):
    if login:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            # "Host": "fantasy.premierleague.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://fantasy.premierleague.com",
            "Referer": referer,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
        }
    else:
        headers = {
            "Host": "fantasy.premierleague.com",
            "Content-Type": "application/json",
            "Origin": "https://fantasy.premierleague.com",
            "Referer": referer,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "X-CSRFToken": self.session.cookies.get('csrftoken', domain='fantasy.premierleague.com')
        }
    return headers