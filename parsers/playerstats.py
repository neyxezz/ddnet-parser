from .utils import _fetch_player_data

class PlayerStatsParser:
    def __init__(self, response):
        self.response = response

    def update(self):
        self.response = _fetch_player_stats_data()

    def _get_activity(self):
        try:
            return self.response["general_activity"]
        except:
            return None

    def _get_playtime_per_month(self):
        activities_list = {}
        try:
            for activity in self.response["playtime_per_month"]:
                activities_list[activity["year_month"]] = activity["seconds_played"]
            return activities_list
        except:
            return None

    def _get_most_played_locations(self):
        locations_list = {}
        try:
            for location in self.response["most_played_locations"]:
                locations_list[location["key"]] = location["seconds_played"]
            return locations_list
        except:
            None

    def _get_most_played_categories(self):
        categories_list = {}
        try:
            for category in self.response["most_played_categories"]:
                categories_list[category["key"]] = category["seconds_played"]
            return categories_list
        except:
            return None

    def _get_most_played_gametypes(self):
        gametypes_list = {}
        try:
            for gametype in self.response["most_played_gametypes"]:
                gametypes_list[gametype["key"]] = gametype["seconds_played"]
            return gametypes_list
        except:
            None

    def _get_favourite_teammates(self):
        favourites_list = {}
        try:
            for favourite in self.response["favourite_teammates"]:
                favourites_list[favourite["name"]] = favourite["ranks_together"]
            return favourites_list if favourites_list else None
        except:
            None

    def _get_recent_finishes(self):
        return self.response["recent_finishes"]

    def get_raw_data(self):
        return self.response

    def get_total_seconds_played(self):
        general_activity = self._get_activity()
        return general_activity["total_seconds_played"]

    def get_start_of_playtime(self):
        general_activity = self._get_activity()
        return general_activity["start_of_playtime"]

    def get_average_seconds_played(self):
        general_activity = self._get_activity()
        return general_activity["average_seconds_played"]

    def get_playtime(self):
        return self._get_playtime_per_month()

    def get_most_played_locations(self):
        return self._get_most_played_locations()

    def get_most_played_categories(self):
        return self._get_most_played_categories()

    def get_most_played_gametypes(self):
        return self._get_most_played_gametypes()

    def get_favourite_teammates(self):
        return self._get_favourite_teammates()

    def get_recent_finishes(self):
        return self._get_recent_finishes()
