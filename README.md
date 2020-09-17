
# WoT Bot

World of tanks discord bot. Does some things (hopefully).

For debugging:

| Attribute    | Example          |
| ------------ | ---------------- |
| `clan_tag`   | `USAGI`          |
| `clan_id`    | `500075018`      |
| `nickname`   | `Natriummangel`* |
| `account_id` | `507295090`      |

**Selected due to being top player by WN8 on the EU server at time of writing*

## Functionality

***

### Server Settings

Each server has it's own settings that are configured by running a command in the channel.

| Setting  | Default | Description                         |
| -------- | ------- | ----------------------------------- |
| `region` | `EU`    | World of tanks region               |
| `clan`   |         | Clan tag used for clan info lookups |

***

### Player & Clan Lookup

Allows a player or clan's statistics to be looked up from the discord channel.

#### Clan

If a clan is found a custom embed will be returned detailing basic statistics about the clans statistics.

* Clan tag and name
* Clan rating
* eSH X, VII, and VI, alongside win rate

#### Player

If a player is found this will return a [wotlabs](https://wotlabs.net/eu) signature image (for a player). An example of one of these is shown below:

![Example signature image](https://wotlabs.net/sig/eu/Some\ random\ dude/signature.png)

***

### Stronghold statistics

#### [SH] Overview

Overview of clan statistics in strongholds. Including:

* Elo rating and win rate for X, VII and VI
* Clan rank and victory points
* Provinces
* Gold over last 28 days
* Influence

#### [SH] Battle history

Display battle history for the given time period. This will have to be capped at a certain number of battles but an overview of the battle statistics can still be displayed.

* Total battles
* Win rate
* Resources gained/lost
* Short list of battles
  * `[XXXX] defeated the [YYYY] clan`

*The above can be accessed from [this](https://eu.wargaming.net/globalmap/#clanlog/CLAN_ID) page*

***

### Global map statistics

#### [GM] Overview

Overview of clan statistics on the global map. Including:

* eGM rating and win rate for X, VII and VI
* Clan rank and victory points
* Provinces
* Gold over last 28 days
* Influence

*The above can be accessed from [this]([@](https://eu.wargaming.net/clans/wot/CLAN_ID/globalmap)) page*

#### [GM] Battle history

Display battle history for the given time period. This will have to be capped at a certain number of battles but an overview of the battle statistics can still be displayed.

* Total battles
* Win rate
* Short list of battles
  * `[XXXX] defeated the [YYYY] clan in a landing tournament for the ZZZZ province.`

*The above can be accessed from [this](https://eu.wargaming.net/globalmap/#clanlog/CLAN_ID) page*

#### [GM] Upcoming battles

Display the clan's battle schedule for the current global map season. This should be reaction controlled to allow a refresh to prevent needing to re-run the command.

* Type (Attack/Defence/Landing)
* Time
* Map and start (North/South, Base 1/2)
* Province
* Enemy Clan

*The above can be accessed from [this](https://eu.wargaming.net/globalmap/#battles/CLAN_ID) page*

***

### Global map notifications

Clans can be watched using a command in the channel, these clans battle logs are posted to the chat. The [clan log](https://eu.wargaming.net/globalmap/#clanlog/CLAN_ID) contains all of the information required.

&nbsp;

&nbsp;

WoT Bot is a free, player created project for [World of Tanks](https://worldoftanks.eu/). It is not an official service of [Wargaming.net](Wargaming.net) or any of its services.<br>World of Tanks is a trademark of [Wargaming.net](Wargaming.net)