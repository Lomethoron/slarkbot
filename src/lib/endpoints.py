from . import request
from src.constants import API_URI_ENDPOINTS


def get_health_check():
    """
    returns response json and status code
    """
    uri = API_URI_ENDPOINTS.HEALTH_CHECK.value
    response = request.make_request(uri)
    return response.json(), response.status_code


def get_match_by_id(id):
    uri = API_URI_ENDPOINTS.MATCHES.value % id
    response = request.make_request(uri)
    return response.json(), response.status_code


def get_players_by_rank():
    uri = API_URI_ENDPOINTS.PLAYERS_BY_RANK.value
    response = request.make_request(uri)
    return response.json(), response.status_code


def get_player_by_account_id(id):
    uri = API_URI_ENDPOINTS.PLAYERS_BY_ACCOUNT_ID.value % id
    response = request.make_request(uri)
    return response.json(), response.status_code


def get_player_recent_matches_by_account_id(id):
    uri = API_URI_ENDPOINTS.PLAYER_RECENTS_BY_ACCOUNT_ID.value % id
    response = request.make_request(uri)
    return response.json(), response.status_code


def get_hero_stats():
    uri = API_URI_ENDPOINTS.HERO_STATS.value
    response = request.make_request(uri)
    return response.json(), response.status_code


def get_constant_data(resource_name):
    uri = API_URI_ENDPOINTS.CONSTANTS.value % resource_name
    response = request.make_request(uri)
    return response.json(), response.status_code
