class Player():
    # a Player object based on the Player's id

    def __init__(self, data):

        self.data = data
        self.id = self.data['id']
        self.first_name = self.data['player_first_name']
        self.last_name = self.data['player_last_name']
        self.team_name = self.data['name']
        self.region = self.data['player_region_name']
        self.gw_points = self.data['summary_event_points']
        self.gw_rank = self.data['summary_event_rank']
        self.total_points = self.data['summary_overall_points']
        self.total_rank = self.data['summary_overall_rank']


    def __repr__(self):
        return f'{self.first_name} {self.last_name} - {self.team_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.team_name}'


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