from .utils import _fetch_master_data

class ClientsParser:
    def __init__(self, response, address):
        self.response = response
        self.address = address
        self._gc = self._get_clients()

    def __str__(self):
        return str(self._gc)

    def update(self):
        self.response = _fetch_master_data()
        self._gc = self._get_clients()

    def _get_clients(self) -> list:
        clients = []
        for server in self.response["servers"]:
            addresses = [x.split("//")[-1] for x in server["addresses"]]
            if not self.address or self.address in addresses:
                for client in server["info"]["clients"]:
                    clients.append(client)
        return clients

    def get_raw_data(self, name: str = None) -> list or None:
        clients = self._gc
        if name:
            for client in clients:
                if client["name"] == name:
                    return client
            return None
        return clients

    def get_clients(self, count: bool = False, types: str = "client") -> list or int:
        clients_list = []
        clients = self._gc
        for client in clients:
            if types=="client":
                is_include = True
            elif types=="player":
                is_include = client["is_player"]
            elif types=="spectator":
                is_include = not client["is_player"]
            else:
                raise ValueError("Unknown type '{}', expected: 'client', 'player' or 'spectator'".format(types))
            if is_include:
                clients_list.append(client)
        if count:
            return len(clients_list) if clients_list else 0
        return clients_list if clients_list else None

    def get_afk_clients(self, count: bool = False, types: str = "client") -> list or int:
        clients = self._gc
        clients_afk_list = []
        for client in clients:
            if types=="client":
                is_include = True
            elif types=="player":
                is_include = client["is_player"]
            elif types=="spectator":
                is_include = not client["is_player"]
            else:
                raise ValueError("Unknown type '{}', expected: 'client', 'player' or 'spectator'".format(types))
            if client.get("afk") and is_include:
                clients_afk_list.append(client)
        if count:
            return len(clients_afk_list) if clients_afk_list else 0
        return clients_afk_list if clients_afk_list else None

    def get_clan(self, name: str) -> str or None:
        clients = self._gc
        for client in clients:
            if client["name"] == name:
                return client.get("clan")
        return None

    def get_team(self, name: str) -> str or None:
        clients = self._gc
        for client in clients:
            if client["name"] == name:
                return client["team"]
        return None

    def get_score(self, name: str) -> str or None:
        clients = self._gc
        for client in clients:
            if client["name"] == name:
                return client["score"]
        return None

    def is_online(self, name: str, types: str = "client") -> bool:
        clients = self._gc
        for client in clients:
            if types=="client":
                is_include = True
            elif types=="player":
                is_include = client["is_player"]
            elif types=="spectator":
                is_include = not client["is_player"]
            else:
                raise ValueError("Unknown type '{}', expected: 'client', 'player' or 'spectator'".format(types))
            if client["name"] == name and is_include:
                return True
        return False

    def get_clients_with_same_clan(self, clan: str, count: bool = False) -> list or int or None:
        clients = self._gc
        clients_with_same_clan = []
        for client in clients:
            if client["clan"] == clan:
                clients_with_same_clan.append(client)
        if count:
            return len(clients_with_same_clan) if clients_with_same_clan else 0
        return clients_with_same_clan if clients_with_same_clan else None

