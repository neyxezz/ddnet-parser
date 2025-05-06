import requests
import json
from .parsers import _fetch_master_data, _fetch_player_data, ServersParser, ClientsParser, PlayerStatsParser

class DDNetMasterParser:
    def __init__(self, address):
        self.response = _fetch_master_data()
        self.servers = ServersParser(self.response, address)
        self.clients = ClientsParser(self.response, address)

class DDNetStatisticsParser:
    def __init__(self, name):
        self.response = _fetch_player_data(name)
        self.stats = PlayerStatsParser(self.response)

def GetServers(address=None):
    master = DDNetMasterParser(address)
    return master.servers

def GetClients(address=None):
    master = DDNetMasterParser(address)
    return master.clients

def GetPlayerStats(name):
    statistics = DDNetStatisticsParser(name)
    return statistics.stats
