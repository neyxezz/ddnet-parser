from .utils import _fetch_map_data

class MapsParser:
    def __init__(self, response, _map):
        self.response = response
        self.map = _map

    def update(self):
        self.response = _fetch_map_data(self.map)

    def _get_info(self):
        return self.response["info"]

    def get_raw_data(self) -> dict:
        return self.response

    def get_finishes(self) -> int:
        info = self._get_info()
        return info["finishes"]

    def get_create_time(self) -> str:
        info = self._get_info()
        return " ".join(info["map"]["timestamp"].split("T"))

    def get_type(self) -> str:
        info = self._get_info()
        return info["map"]["server"]

    def get_points(self) -> int:
        info = self._get_info()
        return info["map"]["points"]

    def get_stars(self) -> int:
        info = self._get_info()
        return info["map"]["stars"]

    def get_mapper(self) -> str:
        info = self._get_info()
        return info["map"]["mapper"]

    def get_median_time(self) -> str:
        info = self._get_info()
        return info["map"]["median_time"]

    def get_playtime(self) -> list:
        return self.response["playtime"]
