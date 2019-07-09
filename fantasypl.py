import requests
import json
import os

from .classes import User, ClassicLeague
from .endpoints import API_BASE_URL, API_URLS

class FPL():
    # A Class for storing the session and wrapping around all functions

    def __init__(self):
        self.session = requests.session()

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

        with self.session.post(login_url, data=payload) as response:
            return response

    def get_my_details(self):
        r = self.session.get(f'{API_BASE_URL}/me/')
        webdata = json.loads(r.text)
        return webdata


    def get_user(self, player_id):
        # Input a player ID (e.g. 68762), output the Player class containing all of their information
        query = f'{API_BASE_URL}/entry/{player_id}/'
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return User(webdata, self.session)


    def get_classicleague(self, league_id):
        # Input a classic league ID, output the ClassicLeague class containing its information
        query = API_URLS['league_classic'].format(league_id)
        r = self.session.get(query)
        webdata = json.loads(r.text)
        return ClassicLeague(webdata, self.session)