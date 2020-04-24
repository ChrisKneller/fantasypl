import requests
import json
import os
import getpass

from .classes import User, ClassicLeague, PLTeam, Footballer
from .endpoints import API_BASE_URL, API_URLS
from .functions import get_headers

class FPL():
    '''
    A Class for storing the session and wrapping around all functions
    '''

    def __init__(self, proxies=None):
        self.session = requests.session()
        self.is_logged_in = False
        self.User = None
        self.players = None
        self.teams = None
        self.proxies = proxies

    
    def __enter__(self):
        return self

    def login(self, email=None, password=None):
        '''
        Log the user in so more capabilities are opened up
        '''

        if not email:
            email = os.environ.get("FPL_EMAIL")
        if not password:
            password = os.environ.get("FPL_PASSWORD")
        
        while not email:
            email = input("Enter your fpl email address: ")
        while not password:
            password = getpass.getpass(f"Enter the password associated with '{email}': ")
        
        assert email and password, "You must enter an email and password"

        login_url = "https://users.premierleague.com/accounts/login/"

        payload = {
            "login": email,
            "password": password,
            "redirect_uri": "https://fantasy.premierleague.com/a/login",
            "app": "plfpl-web",
        }

        headers = get_headers(login=True)

        response = self.session.post(login_url, data=payload, headers=headers, proxies=self.proxies)
        if response.status_code == 200:
            print('Connected to FPL server. Attempting login...')
            player = self.get_my_details()['player']
            if player:
                self.is_logged_in = True
                self.User = self.get_user(player['entry'], logging_in=True)
                print(f'Successfully logged in: {self.User}')
            else:
                print('Invalid login details. Please try again.')
        return response

    def get_my_details(self):
        r = self.session.get(f'{API_BASE_URL}/me/', proxies=self.proxies)
        webdata = json.loads(r.text)
        return webdata


    def get_user(self, player_id, logging_in=False):
        '''
        Input a player ID (e.g. 68762), output the Player class containing all of their information
        '''
        query = f'{API_BASE_URL}/entry/{player_id}/'
        r = self.session.get(query, proxies=self.proxies)
        webdata = json.loads(r.text)
        return User(webdata, self.session, logging_in)


    def get_classicleague(self, league_id):
        '''
        Input a classic league ID, output the ClassicLeague object containing its information
        '''
        return ClassicLeague(league_id, self.session)


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
        print("Getting all players...")
        playerdetails = self.get_staticdata()['elements']
        players = []
        for player in playerdetails:
            new_player = Footballer(player, self.session)
            players.append(new_player)
        self.players = players
        print("Got players")
        return players

    def get_plplayer_by_id(self, players, id):
        return next(player for player in players if player.id == id)

    def get_plplayer_by_name(self, name):
        players = self.players
        if not players:
            if not self.players:
                self.players = self.get_plplayers()
                print("Getting players")
            else:
                players = self.players
                print("Using players already getted")
        return next(player for player in self.players if player.name == name)