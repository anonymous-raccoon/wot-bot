
from .wgapi import WGApplication

def search_players(app:WGApplication, search:str, region:str="EU", limit:int=100):
    resp, error = app.make_request(
        "https://api.worldoftanks.eu/wot/account/list/",
        id_required=True,
        search=search,
        region=region,
        limit=limit
    )

    return resp, error

def search_clans(app:WGApplication, search:str, region:str="EU", limit:int=100):
    resp, error = app.make_request(
        "https://api.worldoftanks.eu/wot/clans/list/",
        id_required=True,
        search=search,
        region=region,
        limit=limit
    )

    return resp, error
