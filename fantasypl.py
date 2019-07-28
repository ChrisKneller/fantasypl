import requests
import json
import os

from .classes import User, ClassicLeague, PLTeam, Footballer
from .endpoints import API_BASE_URL, API_URLS
from .functions import get_headers

class FPL():
    # A Class for storing the session and wrapping around all functions

    def __init__(self):
        self.session = requests.session()
        self.is_logged_in = False
        self.User = None
        self.players = None
        self.teams = None

    
    def __enter__(self):
        return self

    def login(self, email=None, password=None):
        # log the user in so more capabilities are opened up
        if not email and not password:
            email = os.environ.get("FPL_EMAIL")
            password = os.environ.get("FPL_PASSWORD")

        if not email or not password:
            raise ValueError("Login requires an email and password")

        login_url = "https://users.premierleague.com/accounts/login/"

        payload = {
            "login": email,
            "password": password,
            "redirect_uri": "https://fantasy.premierleague.com/a/login",
            "app": "plfpl-web",
        }

        headers = get_headers(login=True)

        response = self.session.post(login_url, data=payload, headers=headers)
        if response.status_code == 200:
            print('Status code 200 aw yiss')
            player = self.get_my_details()['player']
            if player:
                self.is_logged_in = True
                self.User = self.get_user(player['entry'], logging_in=True)
                print(f'Successfully logged in: {self.User}')
            else:
                print('Invalid login details. Please try again.')
        return response

    def get_my_details(self):
        r = self.session.get(f'{API_BASE_URL}/me/')
        webdata = json.loads(r.text)
        return webdata


    def get_user(self, player_id, logging_in=False):
        # Input a player ID (e.g. 68762), output the Player class containing all of their information
        query = f'{API_BASE_URL}/entry/{player_id}/'
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return User(webdata, self.session, logging_in)


    def get_classicleague(self, league_id):
        # Input a classic league ID, output the ClassicLeague class containing its information
        query = API_URLS['league_classic'].format(league_id)
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return ClassicLeague(webdata, self.session)


    def get_staticdata(self):
        query = API_URLS['static']
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return webdata

    
    def get_plteams(self):
        if self.teams:
            print("You already have the teams m8")
            return self.teams
        teamdetails = self.get_staticdata()['teams']
        teams = []
        for team in teamdetails:
            teams.append(PLTeam(team, self.session))
        self.teams = teams
        return teams


    def get_plplayers(self):
        if self.players:
            print("You already have the players m8")
            return self.players
        playerdetails = self.get_staticdata()['elements']
        players = []
        for player in playerdetails:
            new_player = Footballer(player, self.session)
            players.append(new_player)
        self.players = players
        return players

    def get_plplayer_by_id(self, players, id):
        return next(player for player in players if player.id == id)

    def get_plplayer_by_name(self, name, players=False):
        if not players:
            if not self.players:
                players = self.get_plplayers()
                print("Getting players")
            else:
                players = self.players
                print("Using players already getted")
        return next(player for player in players if player.name == name)