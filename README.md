# Simple parser of data from DDNet Master Servers and DDStats

This parser makes it easy to get data from [ddnet master servers](https://master1.ddnet.org/ddnet/15/servers.json) and various statistics from [ddstats.tw](https://ddstats.tw/).

## Installation:
Installing the library:
```
pip install requests
```
Installing the latest stable version of the parser:
```
pip install ddnet-parser
```
Installing test and unstable version of the parser:
```
pip install git+https://github.com/neyxezz/ddnet-parser@tests
```

# get_clients(address=None, data=None)
* Gets an object for parsing client information
* Documentation: [🙂](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#clientsparser-class)
* Args: address(bool, optional): address of the server for which to get client information; data(dict or str, optional): data from which the information will be parsed

Example:
```python
from ddnet_parser import get_clients

clients = get_clients()
print(clients.get_clients(count=True))
```
## get_servers(address=None, data=None)
* Gets an object for parsing server information
* Documentation: [🙂](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#serversparser-class)
* Args: address(bool, optional): address of the server to get information for; data(dict or str, optional): data from which the information will be parsed

Example:
```python
from ddnet_parser import get_servers

servers = get_servers()
print(servers.get_count())
```
## get_player_stats(name)
* Gets an object for parsing player stats
* Documentation: [🙂](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#playerstatsparser-class)
* Args: name(str): the nickname for which you want to get stats

Example:
```python
from ddnet_parser import get_player_stats

player = get_player_stats("neyxezz")
print(player.get_total_seconds_played())
```
## get_map(_map)
* Gets an object for parsing map data
* Documentation: [🙂](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#mapsparser-class)
* Args: address(str): the map to get data for

Example:
```python
from ddnet_parser import get_map

map = get_map("Linear")
print(map.get_mapper())
```
## get_profile(name)
* Gets an object for parsing a player's profile
* Documentation: [🙂](https://github.com/neyxezz/ddnet-parser/blob/main/docs/docs.md#profileparser-class)
* Args: name(str): the nickname to get the profile for

Example:
```python
from ddnet_parser import get_profile

profile = get_profile()
print(profile.get_points())
```
## Detailed documentation with examples:
* Detailed documentation: [🙂](docs/docs.md)
* Examples: [🙂](examples/examples.py)

## Contact me
tg main: @neyxezz, tg twink: @neyxezz_twink
