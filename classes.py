from .endpoints import API_BASE_URL, API_URLS
import json

class User():
    # A User class based on the User's id

    def __init__(self, data, session):

        self.data = data
        self.session = session
        self.id = data['id']
        self.first_name = data['player_first_name']
        self.last_name = data['player_last_name']
        self.team_name = data['name']
        self.region = data['player_region_name']
        self.gw_points = data['summary_event_points']
        self.gw_rank = data['summary_event_rank']
        self.total_points = data['summary_overall_points']
        self.total_rank = data['summary_overall_rank']


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

    # TODO: define methods for (getting) cup, picks, team and transfers


    def get_team(self):
        # return a logged in users current team
        query = API_URLS['user_team'].format(self.id)
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return webdata['picks']


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
