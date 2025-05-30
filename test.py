from ddnet_parser import GetServers

servers = GetServers()
try:
    print(servers.get_map_name())
except Exception as e:
    print(e)