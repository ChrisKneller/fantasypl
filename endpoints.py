API_BASE_URL = "https://fantasy.premierleague.com/api/"

API_URLS = {
    "dynamic": "{}bootstrap-dynamic".format(API_BASE_URL),
    "fixtures": "{}fixtures".format(API_BASE_URL),
    "gameweeks": "{}events".format(API_BASE_URL),
    "gameweek_fixtures": "{}fixtures/?event={{}}".format(API_BASE_URL),
    "gameweek_live": "{}event/{{}}/live".format(API_BASE_URL),
    "h2h": "{}leagues-entries-and-h2h-matches/league/{{}}?page={{}}".format(API_BASE_URL),
    "league_classic": "{}leagues-classic/{{}}/standings/".format(API_BASE_URL),
    "league_classic_new": "{}leagues-classic/{{league}}/standings/?page_new_entries={{page}}&page_standings=1".format(API_BASE_URL),
    "league_classic_standings": "{}leagues-classic/{{league}}/standings/?page_new_entries=1&page_standings={{page}}".format(API_BASE_URL),
    "league_classic_create": "{}leagues-classic/".format(API_BASE_URL),
    "league_delete": "{}leagues-private/delete/".format(API_BASE_URL),
    "league_join": "{}leagues-private/join/".format(API_BASE_URL),
    "league_h2h": "{}leagues-h2h/{{}}/standings/".format(API_BASE_URL),
    "players": "{}elements".format(API_BASE_URL), # NOT IN USE AS OF 25/7/19
    "player": "{}element-summary/{{}}".format(API_BASE_URL),
    "settings": "{}game-settings".format(API_BASE_URL),
    "static": "{}bootstrap-static/".format(API_BASE_URL),
    "teams": "{}teams".format(API_BASE_URL),
    "transfers": "{}transfers/".format(API_BASE_URL),
    "user": "{}entry/{{}}/".format(API_BASE_URL),
    "user_cup": "{}entry/{{}}/cup".format(API_BASE_URL),
    "user_history": "{}entry/{{}}/history/".format(API_BASE_URL),
    "user_picks": "{}entry/{{}}/event/{{}}/picks".format(API_BASE_URL),
    "user_team": "{}my-team/{{}}".format(API_BASE_URL),
    "user_transfers": "{}entry/{{}}/transfers".format(API_BASE_URL),
    "watchlist": "{}watchlist/".format(API_BASE_URL)
}

PICKS_FORMAT = "{} {}{}"
MYTEAM_FORMAT = "{}{}"
