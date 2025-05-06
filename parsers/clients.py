from .utils import _fetch_master_data

class ClientsParser:
    def __init__(self, response, address):
        self.response = response
        self.address = address

    def update(self):
        #updates data from master
        self.response = _fetch_data()

    def _get_clients(self) -> list:
        clients = []
        #get clients in one server if address specified, else all clients in all servers
        for server in self.response["servers"]:
            addresses = [x.split("//")[-1] for x in server["addresses"]]
            if not self.address or self.address in addresses:
                for client in server["info"]["clients"]:
                    clients.append(client)
        return clients

    def get_raw_data(self, name) -> list or None:
        #return client data if address specified, else all clients in one server
        clients = self._get_clients()
        for client in clients:
            if client["name"] == name:
                return client
        return None

    def get_clients(self, count=False) -> list or int:
        clients_list = []
        clients = self._get_clients()
        for client in clients:
            clients_list.append(client)
        if count:
            return len(clients_list)
        return clients_list

    def get_players(self, count=False) -> list or int:
        players_list = []
        clients = self._get_clients()
        for client in clients:
            if client["is_player"]:
                players_list.append(client)
        if count:
            return len(players_list)
        return players_list

    def get_bots(self, count=False) -> list or int:
        bots_list = []
        clients = self._get_clients()
        for client in clients:
            if not client["is_player"]:
                bots_list.append(client)
        if count:
            return len(bots_list)
        return bots_list

    def get_afk_clients(self, count=False) -> list or int:
        clients_afk_list = []
        clients = self._get_clients()
        for client in clients:
            if client.get("afk", False):
                clients_afk_list.append(client)
        if count:
            return len(clients_afk_list)
        return clients_afk_list

    def get_afk_players(self, count=False) -> list or int:
        players_afk_list = []
        clients = self._get_clients()
        for client in clients:
            if client.get("afk", False) and client["is_player"]:
                players_afk_list.append(client)
        if count:
            return len(players_afk_list)
        return players_afk_list

    def get_afk_bots(self, count=False) -> list or int:
        bots_afk_list = 0
        clients = self._get_clients()
        for client in clients:
            if client.get("afk", False) and not client["is_player"]:
                bots_afk_count.append(client)
        if count:
            return len(bots_afk_list)
        return bots_afk_list

    def get_clan(self, name) -> str or None:
        clients = self._get_clients()
        for client in clients:
            if client["name"] == name:
                return client.get("clan")
        return None

    def get_team(self, name) -> str or None:
        clients = self._get_clients()
        for client in clients:
            if client["name"] == name:
                return client.get("team")
        return None

    def is_client_online(self, name) -> bool:
        clients = self._get_clients()
        for client in clients:
            if client["name"] == name:
                return True
        return False

    def is_player_online(self, name) -> bool:
        clients = self._get_clients()
        for client in clients:
            if client["name"] == name and client["is_player"]:
                return True
        return False

    def is_bot_online(self, name) -> bool:
        clients = self._get_clients()
        for client in clients:
            if client["name"] == name and not client["is_player"]:
                return True
        return False
