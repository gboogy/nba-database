import requests
import json

data_url = 'http://data.nba.net/10s'


def convert_str(s):
    if s == '':
        return None
    if s == '-':
        return None
    else:
        return s


def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data


def get_teams() -> dict:
    """ Get all teams from NBA API """
    endpoint = '/prod/v2/2019/teams.json'
    url = data_url + endpoint
    teams_obj = get_data(url).get('league').get('standard', [])
    for team in teams_obj:
        yield {
            "team_id": team["teamId"],
            "name": team["fullName"],
            "city": team["city"],
            "nickname": team["nickname"],
            "conference": team["confName"],
            "division": team["divName"],
            "abbr": team["tricode"],
        }


def get_players() -> dict:
    """ Get all players from NBA API """
    endpoint = '/prod/v1/2019/players.json'
    url = data_url + endpoint
    players_obj = get_data(url).get('league').get('standard', [])
    for player in players_obj:
        yield {
            "player_id": player["personId"],
            "first_name": player["firstName"],
            "last_name": player["lastName"],
            "team_id": convert_str(player["teamId"]),
            "position": player["pos"],
            "jersey": player["jersey"],
            "height_ft": convert_str(player["heightFeet"]),
            "height_in": convert_str(player["heightInches"]),
            "height_m": convert_str(player["heightMeters"]),
            "weight_lbs": convert_str(player["weightPounds"]),
            "weight_kg": convert_str(player["weightKilograms"]),
            "dob_utc": convert_str(player["dateOfBirthUTC"]),
            "draft_round": convert_str(player["draft"].get("roundNum")),
            "draft_pick": convert_str(player["draft"].get("pickNum")),
            "draft_team": convert_str(player["draft"].get("teamId")),
            "draft_year": convert_str(player["draft"].get("seasonYear")),
            "debut_year": convert_str(player["nbaDebutYear"]),
            "years_pro": convert_str(player["yearsPro"]),
            "college": player["collegeName"],
            "last_affiliation": player["lastAffiliation"],
            "country": player["country"],
            "teams": json.dumps(player["teams"]),
            "is_active": player["isActive"],
        }


def get_coaches() -> dict:
    """ Get all coaches from NBA API """
    endpoint = '/prod/v1/2019/coaches.json'
    url = data_url + endpoint
    coaches_obj = get_data(url).get('league').get('standard', [])
    for coach in coaches_obj:
        yield {
            "coach_id": coach["personId"],
            "first_name": coach["firstName"],
            "last_name": coach["lastName"],
            "team_id": coach["teamId"],
            "college": coach["college"],
            "is_assistant": coach["isAssistant"],
        }