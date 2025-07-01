from .utils import _fetch_profile_data

class ProfileParser:
    def __init__(self, response, name):
        self.response = response
        self.name = name

    def update(self):
        self.response = _fetch_profile_data(self.name)

    def __str__(self):
        return str(self.response)

    def get_raw_data(self) -> dict:
        return self.response

    def get_points(self) -> int:
        return self.response["points"]

    def get_clan(self) -> str:
        return self.response["clan"]

    def get_country(self) -> int:
        return self.response["country"]

    def get_skin_name(self) -> str:
        return self.response["skin_name"]

    def get_skin_color_body(self) -> int:
        return self.response["skin_color_body"]

    def get_skin_color_feet(self) -> int:
        return self.response["skin_color_feet"]

