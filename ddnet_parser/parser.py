from .parsers import _fetch_master_data, _fetch_player_data, _fetch_map_data, _fetch_profile_data, ServersParser, ClientsParser, PlayerStatsParser, MapsParser, ProfileParser

class DDNetMasterParser:
    def __init__(self, address):
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

def GetServers(address=None):
    master = DDNetMasterParser(address)
    return master.servers

def GetClients(address=None):
    master = DDNetMasterParser(address)
    return master.clients

def GetPlayerStats(name):
    player = DDNetStatisticsParser(name)
    return player.stats

def GetMap(_map):
    maps = DDNetMapsParser(_map)
    return maps.map

def GetProfile(name):
    profile = DDNetProfileParser(name)
    return profile.data

