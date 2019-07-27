from .endpoints import API_BASE_URL, API_URLS
from .functions import position_id_to_str, team_id_to_str
import json

class User():
    # A User class based on the User's id

    def __init__(self, data, session, logging_in=False):

        self.data = data
        self.session = session
        self.is_logged_in = False if not logging_in else True
        self.id = data['id']
        self.first_name = data['player_first_name']
        self.last_name = data['player_last_name']
        self.team_name = data['name']
        self.region = data['player_region_name']
        self.gw_points = data['summary_event_points']
        self.gw_rank = data['summary_event_rank']
        self.total_points = data['summary_overall_points']
        self.total_rank = data['summary_overall_rank']
        self.current_event = data['current_event']


    def __repr__(self):
        return f'{self.first_name} {self.last_name} - {self.team_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.team_name}'


    def get_classic_leagues(self):
        # return a list of classic league ids that the User is a part of
        classic_leagues = []
        leagues_data = self.data['leagues']['classic']
        for league in leagues_data:
            classic_leagues.append(league['id'])
        return classic_leagues

    def get_h2h_leagues(self):
        # return a list of h2h league ids that the User is a part of
        h2h_leagues = []
        leagues_data = self.data['leagues']['h2h']
        for league in leagues_data:
            h2h_leagues.append(league['id'])
        return h2h_leagues


    def get_gameweek_history(self):
        # return a user's full gameweek scoring history
        query = API_URLS['user_history'].format(self.id)
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return webdata['current']

    
    def get_season_history(self):
        # return a user's full season scoring history
        query = API_URLS['user_history'].format(self.id)
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return webdata['past']


    def get_team(self):
        # return a logged in user's current team
        query = API_URLS['user_team'].format(self.id)
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return webdata['picks']

    # TODO: define methods for (getting) cup


    # TODO: add wildcard transfers functionality
    def get_transfer_payload(self, players_out, players_in, user_team, players, wildcard):
        # returns the payload needed to make the requested transfers
        payload = {
            "chip": None,
            "entry": self.id,
            "event": (self.current_event + 1) if self.current_event else 1, # current event i.e. gw is False if season hasn't started
            "transfers": [],
            # "wildcard": wildcard,
            # "freehit": False
            }

        for player_out_id, player_in_id in zip(players_out, players_in):
            player_out = next(player for player in user_team
                            if player["element"] == player_out_id)
            player_in = next(player for player in players
                            if player["id"] == player_in_id)
            payload["transfers"].append({
                "element_in": player_in["id"],
                "element_out": player_out["element"],
                "purchase_price": player_in["now_cost"],
                "selling_price": player_out["selling_price"]
        })

        return payload


    def transfer(self, players_out, players_in, max_hit=12, wildcard=False):
        # method for making transfers for the logged in player
        
        # cover various error cases
        if not self.is_logged_in:
            raise Exception("User is not logged in")

        if not players_out or not players_in:
            raise Exception("You must transfer at least one player in and one player out")

        if len(players_out) != len(players_in):
            raise Exception("You must transfer the same amount of players in and out")

        # get the player's own team
        team = self.get_team()

        # get the list of all players
        players_query = API_URLS['static']
        players_r = self.session.get(players_query)
        players = json.loads(players_r.text)['elements']

        # these headers have been tested and are working as of gameweek 0 in season 19/20
        headers = {
            "Host": "fantasy.premierleague.com",
            "Content-Type": "application/json",
            "Origin": "https://fantasy.premierleague.com",
            "Referer": "https://fantasy.premierleague.com/transfers",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
            "X-CSRFToken": self.session.cookies.get('csrftoken', domain='fantasy.premierleague.com')
        }

        # get the payload to send with the post request
        payload = self.get_transfer_payload(players_out, players_in, team, players, wildcard)

        # get the transfer URL for the post request
        transfer_url = API_URLS["transfers"]

        with self.session.post(transfer_url, data=json.dumps(payload), headers=headers) as response:
            if response.status_code == 200:
                print('Status code 200 aw yiss')
            return response

class ClassicLeague():
    # A class based on a classic league

    def __init__(self, data, session):
        self.data = data
        self.session = session
        self.id = data['league']['id']
        self.name = data['league']['name']

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class PLTeam():
    # A class for the premier league teams (Arsenal, Aston Villa etc.)

    def __init__(self, data, session):
        self.data = data
        self.session = session
        self.id = data['id']
        self.name = data['name']
        self.shortname = data['short_name']
        self.strength = data['strength']
        formkeys = ['strength_overall_home', 'strength_attack_home', 'strength_defence_home',
                    'strength_overall_away', 'strength_attack_away', 'strength_defence_away']
        self.form = {key:self.data[key] for key in formkeys if key in self.data}

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'

# TODO: define Player (Footballer) class for readability when returning a user's team


class Footballer():
    # A class for the premier league footballers

    def __init__(self, data, session):
        self.data = data
        self.session = session
        self.id = data['id']
        self.position_id = data['element_type']
        self.position = position_id_to_str(self.position_id)
        self.first_name = data['first_name'] if data['first_name'] else None
        self.last_name = data['second_name'] if data['second_name'] else None
        self.name = data['web_name']
        self.team_id = data['team']
        self.team = team_id_to_str(self.team_id)

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'

# Example data for a Player:
#  {'assists': 1,
#   'bonus': 3,
#   'bps': 156,
#   'chance_of_playing_next_round': None,
#   'chance_of_playing_this_round': None,
#   'clean_sheets': 1,
#   'code': 166324,
#   'cost_change_event': 0,
#   'cost_change_event_fall': 0,
#   'cost_change_start': 0,
#   'cost_change_start_fall': 0,
#   'creativity': '313.6',
#   'dreamteam_count': 0,
#   'element_type':3,
#   'ep_next': None,
#   'ep_this': None,
#   'event_points': 0,
#   'first_name': 'Ivan',
#   'form': '0.0',
#   'goals_conceded': 11,
#   'goals_scored': 3,
#   'ict_index': '66.0',
#   'id': 419,
#   'in_dreamteam': False,
#   'influence': '198.0',
#   'minutes': 677,
#   'news': '',
#   'news_added': None,
#   'now_cost': 50,
#   'own_goals': 0,
#   'penalties_missed': 0,
#   'penalties_saved': 0,
#   'photo': '166324.jpg',
#   'points_per_game': '2.1',
#   'red_cards': 0,
#   'saves': 0,
#   'second_name': 'Cavaleiro',
#   'selected_by_percent': '0.1',
#   'special': False,
#   'squad_number': None,
#   'status': 'a',
#   'team': 20,
#   'team_code': 39,
#   'threat': '156.0',
#   'total_points': 48,
#   'transfers_in': 0,
#   'transfers_in_event': 0,
#   'transfers_out': 0,
#   'transfers_out_event': 0,
#   'value_form': '0.0',
#   'value_season': '0.0',
#   'web_name': 'Cavaleiro',
#   'yellow_cards': 1},