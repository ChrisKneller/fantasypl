import requests
import json
from pprint import pprint

base_url = 'https://fantasy.premierleague.com/api'


# input league number; output league details (e.g. 68762)
def get_player_details(league_id):
    r = requests.get(f'{base_url}/entry/{league_id}/')
    webdata = json.loads(r.text)
    webdata = pprint(webdata)
    return webdata