from .utils import _fetch_master_data

class ServersParser:
    def __init__(self, response, address):
        self.response = response
        self.address = address

    def update(self):
        self.response = _fetch_master_data()

    def _get_server_by_address(self) -> dict or None:
        if not self.address:
            raise ValueError("No address specified in GetServers func")
        for server in self.response["servers"]:
            if self.address in [x.split("//")[-1] for x in server["addresses"]]:
                return server
        return None

    def get_raw_data(self) -> dict:
        if self.address:
            server = self._get_server_by_address()
            return server
        return self.response["servers"]

    def get_count(self) -> int:
        return len(self.response["servers"])

    def get_passworded_servers(self, count: bool = False) -> list or int:
        passworded_servers = []
        for server in self.response["servers"]:
            if server["info"]["passworded"]:
                passworded_servers.append(server)
        if passworded_servers:
            return len(passworded_servers) if count else passworded_servers
        return None

    def get_require_login_servers(self, count: bool = False) -> list or int:
        require_login_servers = []
        for server in self.response["servers"]:
            if server["info"].get("requires_login", False):
                require_login_servers.append(server)
        if require_login_servers:
            return len(require_login_servers) if count else require_login_servers
        return None

    def get_location(self) -> str or None:
        server = self._get_server_by_address()
        if server:
            return server["location"]
        return None

    def get_max_clients(self) -> int or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["max_clients"]
        return None

    def get_max_players(self) -> int or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["max_players"]
        return None

    def get_game_type(self) -> str or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["game_type"]
        return None

    def get_name(self) -> str or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["name"]
        return None

    def get_map_name(self) -> str or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["map"]["name"]
        return None

    def get_map_hash(self) -> str or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["map"]["sha256"]
        return None

    def get_map_size(self) -> str or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["map"]["size"]
        return None

    def get_version(self) -> str or None:
        server = self._get_server_by_address()
        if server:
            return server["info"]["version"]
        return None

    def is_require_login(self) -> bool:
        server = self._get_server_by_address()
        if server:
            return server["info"]["requires_login"]
        return None

    def is_passworded(self) -> bool:
        server = self._get_server_by_address()
        if server:
            return server["info"]["passworded"]
        return None

    def get_server_by_client_name(self, name: str, all_servers: bool = False) -> dict or None:
        servers = []
        for server in self.response["servers"]:
            for client in server["info"]["clients"]:
                if client["name"] == name:
                    if not all_servers:
                        return server
                    servers.append(server)
                    break
        return servers if servers else None

    def get_servers_by_game_type(self, game_type: str, count: bool = False) -> list:
        servers = []
        for server in self.response["servers"]:
            if server["info"]["game_type"] == game_type:
                servers.append(server)
        if servers:
            return len(servers) if count else servers
        return None

    def get_servers_by_location(self, location: str, count: bool = False) -> list:
        servers = []
        for server in self.response["servers"]:
            if server["info"]["location"] == location:
                servers.append(server)
        if servers:
            return len(servers) if count else servers
        return None

    def get_servers_by_map_name(self, map_name: str, count: bool = False) -> list:
        servers = []
        for server in self.response["servers"]:
            if server["info"]["map"]["name"] == map_name:
                servers.append(server)
        if servers:
            return len(servers) if count else servers
        return None
