## Navigation:
- [get_clients](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#clientsparser-class)
- [get_servers](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#serversparser-class)
- [get_player_stats](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#playerstatsparser-class)
- [get_map](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#mapsparser-class)
- [get_profile](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#profileparser-class)

## Updating data with update()
For each class object, you can use the `update()` function to update the data.

Example:
```python
from ddnet_parser import get_clients
import time

clients = get_clients()
print(clients.get_clients(count=True))
time.sleep(10)
clients.update()
print(clients.get_clients(count=True)))
```

## Using existing data
At the moment, you can use existing data in DDNetMasterParser without parsing fresh data from master1.ddnet.org. Every 5 minutes, starting with 3 minutes from daystart, data from master tracked [here](https://ddnet.org/stats/master/). You can also download archives with data from master for past days and use it.

Example:
```python
from ddnet_parser import get_servers

with open("00_00_03.json") as f:
    servers_data = f.read()

servers = get_servers(data=servers_data)
print(servers.get_count())
```

Important note: Make sure you provide the correct data, dictionary or string representing dictionary

# ClientsParser class
Example usage:
```python
from ddnet_parser import get_clients

clients = get_clients()
print(clients.get_clients(count=True))
```
### Functions to the get_clients() object of the ClientsParser class:
## get_raw_data(name).

* Description: Gets the raw data of a client by its name
* Arguments:
    * name (str): The client's name
* Features: If an address is given, returns the client specifically at that address, otherwise, the first occurrence.
* Returns: dict or None: dictionary with client data if client is found, otherwise None
```python
clients = get_clients("ip:port")
print(clients.get_raw_data("nameless tee"))
```
## get_clients(count=False, types="client")

* Description: Gets a list of all clients by the given type.
* Features: If the address is given in the get_clients function, returns all clients of the server, otherwise all clients of all servers. The main types of clients for the types variable are:
    - client (all clients);
    - player (regular players);
    - spectator (spectators)
Note that connecting clients are also spectators and are marked with the nickname `(connecting)`.
* Arguments:
    * count (bool, optional): If True, returns the number of clients. Defaults to False
    * types (str, optional): Client type.
* Returns: list or int: list of dictionaries with client information or number of clients if count=True
```python
clients = get_clients("ip:port")
print(clients.get_clients(types="spectator"))
```
## get_afk_clients(count=False, types="client")

* Description: Gets a list of all AFK clients
* Features: If the address is given in the get_clients function, returns all clients of the server, otherwise all clients of all servers. The main types of clients for the types variable are:
    - client (all clients);
    - player (regular players);
    - spectator (spectators)
Note that connecting clients are also spectators and are marked with the nickname `(connecting)`.
* Arguments:
    * count (bool, optional): If True, returns the number of AFK clients. Defaults to False
    * types (str, optional): Client type.
* Returns: list or int: list of dictionaries with AFK client information or number of AFK clients if count=True
```python
clients = get_clients("ip:port")
print(clients.get_afk_clients(types="spectator"))
```
## get_clan(name)

* Description: Gets the client's clan by name
* Arguments:
    * name (str): Client's name
* Returns: str or None: client clan name if client is found, otherwise None
```python
clients = get_clients("ip:port")
print(clients.get_clan("nameless tee"))
```
## get_team(name)

* Description: Gets the client's team by name
* Arguments:
    * name (str): The client's name
* Returns: str or None: client team if client is found, otherwise None
```python
clients = get_clients("ip:port")
print(clients.get_team("nameless tee"))
```
## get_score(name)

* Description: Gets the client's scores by name
* Arguments:
    * name (str): The client's name
* Returns: str or None: client's team name if client is found, otherwise None
```python
clients = get_clients("ip:port")
print(clients.get_team("nameless tee"))
```
## is_online(name, types="client")

* Description: Checks if the client is online by name
* Features: If the address is given in the get_clients function, returns all clients of the server, otherwise all clients of all servers. The main types of clients for the types variable are:
    - client (all clients);
    - player (regular players);
    - spectator (spectators)
Note that connecting clients are also spectators and are marked with the nickname `(connecting)`.
* Arguments:
    * name (str): Client name
    * types (str, optional): Client type
* Returns: bool: True if client is online, otherwise False
```python
clients = get_clients("ip:port")
print(clients.is_online("nameless tee", types="spectator")))
```
## get_clients_with_same_clan(clan)

* Description: Gets a list of clients with the given clan
* Arguments: str: clan
```python
from ddnet_parser import get_clients

clients = get_clients()
print(clients.get_clients_with_same_clan("clan"))
```
# ServersParser class

Example usage:
```python
from ddnet_parser import get_servers

server = get_servers("ip:port")
print(server.get_name())
```
### Functions to the get_servers() object of the ServersParser class:
## get_raw_data()

* Description: Gets the raw data of a server or all servers
* Features: If an address is given, returns data at that address, otherwise returns data from all servers
* Arguments: None
* Returns: dict or list: dictionary with server data if address is given, otherwise dictionary list with all servers
```python
servers = get_servers()
print(servers.get_raw_data())
```
## get_count()

* Description: Gets the total number of servers.
* Arguments: None
* Returns: int: total number of servers.
```python
servers = get_servers()
print(servers.get_count())
```
## get_passworded_servers(count=False)

* Description: Gets the list of servers requiring a password
* Arguments: count (bool, optional): If True, returns the number of servers with password. Default is False
* Returns: list or int: list of dictionaries containing data about servers with password or their number if count=True
```python
servers = get_servers()
print(servers.get_passworded_servers())
print(servers.get_passworded_servers(count=True)))
```
## get_require_login_servers(count=False)

* Description: Gets a list of servers that require a login
* Arguments: count (bool, optional): If True, returns the number of servers with a password. Default is False
* Returns: list or int: a list of dictionaries with data about servers with password or their number if count=True
```python
servers = get_servers()
print(servers.get_require_login_servers())
```
## get_location()

* Description: Gets server location
* Feature: This function only works if the address was defined in get_servers.
* Arguments: None
* Returns: str: server location
```python
servers = get_servers()
print(servers.get_location())
```
## get_max_clients()

* Description: Gets the maximum number of clients on the server
* Feature: This function works only when the address was defined in get_servers
* Arguments: None
* Returns: int: maximum number of clients
```python
servers = get_servers()
print(servers.get_max_clients())
```
## get_max_players()

* Description: Gets the maximum number of players on the server
* Feature: This function only works when the address was defined in get_servers
* Arguments: None
* Returns: int: maximum number of players
```python
servers = get_servers()
print(servers.get_max_players())
```
## get_game_type()

* Description: Gets the game type on the server
* Feature: This function only works if the address was defined in get_servers.
* Arguments: None
* Returns: str: game type
```python
servers = get_servers()
print(servers.get_game_type())
```
## get_name()

* Description: Gets the name of the server
* Feature: This function only works if the address was defined in get_servers.
* Arguments: None
* Returns: str: server name
```python
servers = get_servers()
print(servers.get_name())
```
## get_map_name()

* Description: Gets the map name
* Feature: This function only works if the address was defined in get_servers.
* Arguments: None
* Returns: str: map name
```python
servers = get_servers()
print(servers.get_map_name())
```
## get_map_hash()

* Description: Gets the map SHA256
* Feature: This function only works if the address was defined in get_servers
* Arguments: None
* Returns: str: SHA256
```python
servers = get_servers()
print(servers.get_map_hash())
```
## get_map_size()

* Description: Gets the map size in bytes
* Feature: This function only works when the address was defined in get_servers
* Arguments: None
* Returns: str: map_size
```python
servers = get_servers()
print(servers.get_map_size())
```
## get_version()

* Description: Gets the server version
* Feature: This function only works if the address was defined in get_servers
* Arguments: None
* Returns: str: server version
```python
servers = get_servers()
print(servers.get_version())
```
## is_require_login()

* Description: Checks if login is required on the server
* Feature: This function only works if the address was defined in get_servers
* Arguments: None
* Returns: bool: True if login is required, otherwise False
```python
servers = get_servers()
print(servers.is_require_login())
```
## is_passworded()

* Description: Checks if the server is passworded.
* Feature: This function works only when the address was defined in get_servers.
* Arguments: None
* Returns: bool: True if the server is passworded, otherwise False
```python
servers = get_servers("ip:port")
print(servers.is_passworded())
```
## get_server_by_client_name(name, all_servers=False)

* Description: Gets server by client nickname
* Arguments: name (str): Client nickname; all_servers (bool, optional): If True, takes all servers with the given client nickname, otherwise first occurrence
* Returns: list: server/servers
```python
servers = get_servers()
print(servers.get_server_by_client_name("nameless tee", all_servers=True))
```
## get_servers_by_game_type(game_type, count=False)

* Description: Gets servers with the specified game type
* Arguments: game_type (str): Game type
* Returns: list: server/servers
```python
server = get_servers()
print(server.get_servers_by_game_type("DDRaceNetwork"))
```
## get_servers_by_location(location, count=False)

* Description: Gets servers with the specified location
* Arguments: location (str): Location
* Returns: list: server/servers
```python
server = get_servers()
print(server.get_servers_by_location("DDRaceNetwork"))
```
## get_servers_by_map_name(map_name, count=False)

* Description: Gets servers with the specified map name
* Arguments: map_name (str): Map name
* Returns: list: server/servers
```python
server = get_servers()
print(server.get_servers_by_map_name("Stronghold"))
```
## get_servers_by_clients_count(start, end, count=False)

* Description: Gets servers by clients count
* Arguments: start (int): start of range; end (int): end of range
* Returns: list: server/servers
```python
servers = get_servers()
s_ = servers.get_servers_by_clients_count(60, 63, True))
```
# PlayerStatsParser class

Example usage:
```python
from ddnet_parser import get_player_stats

player_stats = get_player_stats("nameless tee")

total_seconds = player_stats.get_total_seconds_played()
print(total_seconds)
```
Important note: not all statistics are always tracked by ddstats.tw, especially if you have a lot of data. So, for example, for the nickname **nameless tee** the functions `get_total_seconds_played`, `get_start_of_playtime`, `get_average_seconds_played`, `get_playtime` return None or an empty list, always take this into account.
### Functions to the get_player_stats() object of the PlayerStatsParser class:
### get_raw_data()

* Description: Gets raw player data
* Arguments: None
* Returns: dict: dictionary with player data
```python
player = get_player_stats("nameless tee")
print(player.get_raw_data())
```
## get_raw_recent_activity_data()

* Description: Gets raw player activity data
* Arguments: None
* Returns: list: list with servers
```python
player = get_player_stats("neyxezz")
print(player.get_raw_recent_activity_data()))
```
## get_total_seconds_played()

* Description: Gets the total number of seconds played in the game
* Arguments: None
* Returns: int: total number of seconds
```python
player = get_player_stats("nameless tee")
print(player.get_total_seconds_played()))
```
## get_start_of_playtime()

* Description: Gets the date of the first appearance in the game
* Arguments: None
* Returns: str: Returns the start date of the game time
```python
player = get_player_stats("nameless tee")
print(player.get_start_of_playtime())
```
## get_average_seconds_played()

* Description: Gets the average number of seconds spent in the game per day
* Arguments: None
* Returns: int: average number of seconds
```python
player = get_player_stats("nameless tee")
print(player.get_average_seconds_played()))
```
## get_playtime()

* Description: Gets playtime data by month
* Arguments: None
* Returns: dict: dictionary where key is year and month, value is number of seconds
```python
player = get_player_stats("nameless tee")
print(player.get_playtime())
```
## get_most_played_locations()

* Description: Gets data about the most frequently played server locations
* Arguments: None
* Returns: dict: dictionary where key is the location, value is the number of seconds
```python
player = get_player_stats("nameless tee")
print(player.get_most_played_locations())
```
## get_most_played_categories()

* Description: Gets data about the most played card categories
* Arguments: None
* Returns: dict: dictionary where key is category, value is number of seconds
```python
player = get_player_stats("nameless tee")
print(player.get_most_played_categories())
```
## get_most_played_gametypes()

* Description: Gets data about the most frequently played game types
* Arguments: None
* Returns: dict: dictionary where key is game type, value is number of seconds
```python
player = get_player_stats("nameless tee")
print(player.get_most_played_gametypes())
```
## get_favourite_teammates()

* Description: Gets data about the teammates with whom you ranked together on the map
* Arguments: None
* Returns: dict: dictionary where key is the name of the teammate, value is the number of games played together
```python
player = get_player_stats("nameless tee")
print(player.get_favourite_teammates())
```
## get_recent_finishes()

* Description: Gets data about the most recently completed maps
* Arguments: None
* Returns: list: a list with data about the most recently completed games
```python
player = get_player_stats("nameless tee")
print(player.get_recent_finishes())
```

# MapsParser class

Example usage:
```python
from ddnet_parser import get_map

map = get_map("Linear")
print(map.get_mapper())
```

### Functions to the get_map() object of the MapsParser class:
## get_raw_data()

* Description: Gets raw player data
* Arguments: None
* Returns: dict: dictionary with player data
```python
map = get_map("Linear")
print(player.get_raw_data())
```
## get_finishes()

* Description: Gets the number of finishes of the map
* Arguments: None
* Returns: int: number of map finishes
```python
map = get_map("Linear")
print(player.get_finishes())
```
## get_create_time()

* Description: Gets the map release date
* Arguments: None
* Returns: str: map release date
```python
map = get_map("Linear")
print(player.get_create_time())
```
## get_type()

* Description: Gets the server type - `Novice`, `Moderate`, `Brutal`, `Insane`....
* Arguments: None
* Returns: str: server type
```python
map = get_map("Linear")
print(player.get_type())
```
## get_points()

* Description: Gets the number of points you get when traversing the map
* Returns: int: number of points
```python
map = get_map("Linear")
print(player.get_points())
```
## get_stars()

* Description: Gets the number of stars on the map
* Arguments: None
* Returns: int: number of stars
```python
map = get_map("Linear")
print(player.get_stars())
```
## get_mapper()

* Description: Gets the map creator
* Arguments: None
* Returns: str: map creator
```python
map = get_map("Linear")
print(player.get_mapper())
```
## get_median_time()

* Description: Gets the average time of a flight to the finish line
* Arguments: None
* Returns: int: average time to finish
```python
map = get_map("Linear")
print(player.get_median_time())
```
## get_playtime()

* Description: Gets the top played seconds.
* Arguments: None
* Returns: list: list with the top of played seconds on the map
```python
map = get_map("Linear")
print(player.get_playtime()))
```
# ProfileParser class

Example usage:
```python
from ddnet_parser import get_profile

profile = get_profile("neyxezz")
print(profile.get_skin_color_body())
```

### Functions to the get_profile() object of the ProfileParser class:
## get_raw_data()

* Description: Gets raw data about the player's profile
* Arguments: None
* Returns: dict: dictionary with player profile
```python
profile = get_profile("neyxezz")
print(profile.get_raw_data())
```
## get_points()

* Description: Gets the total number of points
* Arguments: None
* Returns: int: number of points
```python
profile = get_profile("neyxezz")
print(profile.get_points())
```
## get_clan(name)

* Description: Gets the client's clan by name
* Arguments:
    * name (str): Client's name
* Returns: str or None: client clan name if client is found, otherwise None
```python
profile = get_profile("nameless tee")
print(profile.get_clan())
```
## get_country()

* Description: Gets the country code
* Arguments: None
* Returns: int: country code
```python
profile = get_profile("neyxezz")
print(profile.get_country())
```
## get_skin_name()

* Description: Gets the name of the skin
* Arguments: None
* Returns: str: skin name
```python
profile = get_profile("neyxezz")
print(profile.get_skin_name())
```
## get_skin_colour_body()

* Description: Gets the body colour code in decimal representation
* Arguments: None
* Returns: int: colour code
```python
profile = get_profile("neyxezz")
print(profile.get_skin_color_body()))
```
## get_skin_color_feet()

* Description: Gets the leg colour code in decimal representation
* Arguments: None
* Returns: int: colour code
```python
profile = get_profile("neyxezz")
print(profile.get_skin_color_feet()))
```