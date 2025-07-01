from .parsers import (
    _fetch_master_data,
    _fetch_player_data,
    _fetch_map_data,
    _fetch_profile_data,
    ServersParser,
    ClientsParser,
    PlayerStatsParser,
    MapsParser,
    ProfileParser
)
import json

class DDNetMasterParser:
    def __init__(self, address, data):
        if data and isinstance(data, dict):
            self.response = data
        else:
            self.response = _fetch_master_data()
        self.servers = ServersParser(self.response, address)
        self.clients = ClientsParser(self.response, address)

class DDNetStatisticsParser:
    def __init__(self, name):
        self.response = _fetch_player_data(name)
        self.stats = PlayerStatsParser(self.response, name)

class DDNetMapsParser:
    def __init__(self, _map):
        self.response = _fetch_map_data(_map)
        self.map = MapsParser(self.response, _map)

class DDNetProfileParser:
    def __init__(self, name):
        self.response = _fetch_profile_data(name)
        self.data = ProfileParser(self.response, name)

def get_servers(address=None, data=None):
    if isinstance(data, str) and data:
        try:
            data = json.loads(data)
            if not isinstance(data, dict):
                raise ValueError("String data does not represent a dictionary")
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON string: %s" % str(e))
        except Exception as e:
            raise e
    else:
        if not isinstance(data, dict) and data:
            raise ValueError("Invalid data for '%s', given '%s', expected 'dict' or 'str' with dictionary" % (__name__, type(data).__name__))
    master = DDNetMasterParser(address, data)
    return master.servers

def get_clients(address=None, data=None):
    if isinstance(data, str) and data:
        try:
            data = json.loads(data)
            if not isinstance(data, dict):
                raise ValueError("String data does not represent a dictionary")
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON string: %s" % str(e))
        except Exception as e:
            raise e
    else:
        if not isinstance(data, dict) and data:
            raise ValueError("Invalid data for '%s', given '%s', expected 'dict' or 'str' with dictionary" % (__name__, type(data).__name__))
    master = DDNetMasterParser(address, data)
    return master.clients

def get_player_stats(name):
    player = DDNetStatisticsParser(name)
    return player.stats

def get_map(_map):
    maps = DDNetMapsParser(_map)
    return maps.map

def get_profile(name):
    profile = DDNetProfileParser(name)
    return profile.data

