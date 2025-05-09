from .utils import _fetch_player_data

class PlayerStatsParser:
    def __init__(self, response, name):
        self.response = response
        self.name = name

    def update(self):
        self.response = _fetch_player_data(self.name)

    def _get_activity(self) -> dict:
        try:
            return self.response["general_activity"]
        except:
            return None

    def _get_playtime_per_month(self) -> list:
        try:
            return self.response["playtime_per_month"]
        except:
            return None

    def _get_most_played_locations(self) -> list:
        try:
            return self.response["most_played_locations"]
        except:
            return None

    def _get_most_played_categories(self) -> list:
        try:
            return self.response["most_played_categories"]
        except:
            return None

    def _get_most_played_gametypes(self) -> list:
        try:
            return self.response["most_played_gametypes"]
        except:
            return None

    def _get_favourite_teammates(self) -> list:
        try:
            return self.response["favourite_teammates"]
        except:
            return None

    def _get_recent_finishes(self) -> list:
        try:
            return self.response["recent_finishes"]
        except:
            return None

    def get_raw_data(self) -> dict:
        return self.response

    def get_total_seconds_played(self) -> int:
        general_activity = self._get_activity()
        if general_activity:
            return general_activity["total_seconds_played"]
        return None

    def get_start_of_playtime(self) -> str:
        general_activity = self._get_activity()
        if general_activity:
            return general_activity["start_of_playtime"]
        return None

    def get_average_seconds_played(self) -> int:
        general_activity = self._get_activity()
        if general_activity:
            return general_activity["average_seconds_played"]
        return None

    def get_playtime(self) -> list:
        return self._get_playtime_per_month()

    def get_most_played_locations(self) -> list:
        return self._get_most_played_locations()

    def get_most_played_categories(self) -> list:
        return self._get_most_played_categories()

    def get_most_played_gametypes(self) -> list:
        return self._get_most_played_gametypes()

    def get_favourite_teammates(self) -> list:
        return self._get_favourite_teammates()

    def get_recent_finishes(self) -> list:
        return self._get_recent_finishes()
