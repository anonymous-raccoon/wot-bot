
# Function plan

List of requirements alongside the endpoints that can be used to gather the information required to complete them.

***

## Player Lookup

### `search_players`

Search for a player using their nickname. Returns a list of possible matches.

```url
https://api.worldoftanks.eu/wot/account/list/?application_id=_______&search=_______&limit=_______
```

#### Arguments

* `api_application: WGApplication` Wargaming application object.
* `search: str` Search term (e.g. `PlayerKiller12354`). Longer than 3 characters, less than 24.
* `region="EU": str` Region to be searched.
* `limit=100: int` Maximum number of returns.

#### Returns

* `dict` Dictionary containing list of players

&nbsp;

&nbsp;

### `get_player_sig`

Get the URL for a player signature.

#### Arguments

* `nickname: str` Player nickname (e.g. `PlayerKiller12354`)
* `region="EU":str` Region of player

#### Returns

* `str` URL of player signature provided by [wotlabs](https://wotlabs.net/eu)

&nbsp;

***

## Clan Lookup

### `search_clans`

Search for a clan using their clan tag. Returns a list of possible matches.

```
https://api.worldoftanks.eu/wot/clans/list/?application_id=_______&search=_______&limit=_______
```

#### Arguments

* `api_application: WGApplication` Wargaming application object.
* `search: str` Search term (e.g. `FAME`). Longer than 3 characters, less than 24.
* `region="EU": str` Region to be searched.
* `limit=100: int` Maximum number of returns.

#### Returns

* `dict` Dictionary containing list of clans

&nbsp;

&nbsp;

### `get_clan_info`

Get the information for a given clan ID.

```
https://eu.wargaming.net/clans/wot/___clan_id___/api/claninfo/
```

#### Arguments

* `api_application: WGApplication` Wargaming application object.
* `clan_id: int` Clan ID
* `region="EU":str` Region of clan

#### Returns

* `dict` Dictionary containing information about the clan

&nbsp;

***

!! - **This feature list is likely to be out of date, please see the main README for a full feature list** - !!
